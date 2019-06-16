from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from middleware.models import Device, TriggerEvent, Scope, Segment, Field
from middleware.serializers import DeviceSerializer
from hl7parser.director import call_hl7_director
from mllp.client import send_message
from hl7parser.logger import Logger
from middleware.models import Client
import datetime

@api_view(['GET'])
def device_details(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response("Not found", status=status.HTTP_404_NOT_FOUND)
    
    serializer = DeviceSerializer(device)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def parse_request(request):
    data = upper_keys(JSONParser().parse(request))   
    if is_request_valid(data):
        modify_valid_data(data)
        client = check_key(data)
        if client:
            device = Device.objects.get(pk=data["META_DATA"]["DEVICE"])
            message = call_hl7_director(data)
            for segments in message.children:
                print(segments.value)
            res = send_message(device.ip, int(device.port), call_hl7_director(data))
            
            # Logger.log(res, client)
            Logger.log("Ok", client)
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response("UnAuthorized", status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)  

def is_request_valid(data):
    if all(elem in data["META_DATA"].keys() for elem in ["TE","DEVICE","SCOPE"]):
        if is_device_valid(data["META_DATA"]["DEVICE"]) and is_capability_valid(data):
            return True
    return False

def is_device_valid(pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return False
    return True

def is_capability_valid(data):

    device, te, scope = request_meta_data(data["META_DATA"])
    segments = Segment.objects.filter(scope=scope)
    for segment in segments:
        if segment.name not in data["DATA"].keys():
            return False
        else:
            fields = Field.objects.filter(segment=segment)
            for field in fields:
                if field.name not in data["DATA"][segment.name]:
                    return False
    return True

def modify_valid_data(data):
    data =  delete_components(data)
    data = modify_date(data)
    return data

def delete_components(data):
    components_to_delete = ["NAME_VALIDITY_RANGE", "ADDRESS_VALIDITY_RANGE"]
    for segment in data["DATA"]:
        for field in data["DATA"][segment]:
            if type(data["DATA"][segment][field]) is dict:
                for element in components_to_delete:
                    data["DATA"][segment][field].pop(element , None)
    return data

def modify_date(data):
    components_to_modify = ["EXPIRATION_DATE", "EFFECTIVE_DATE", "TIME"]
    for segment in data["DATA"]:
        for field in data["DATA"][segment]:
            if type(data["DATA"][segment][field]) is dict:
                for element in components_to_modify:
                    if element in  data["DATA"][segment][field].keys():
                        date = guess_date(data["DATA"][segment][field][element])
                        data["DATA"][segment][field][element] =  date.strftime("%Y%m%d")
                
    return data

def request_meta_data(data):
    device = Device.objects.get(pk=data["DEVICE"])
    te = TriggerEvent.objects.get(device=device, code=data["TE"])
    scope = Scope.objects.get(trigger_event=te, code=data["SCOPE"])
    return device, te, scope

def guess_date(string):
    for fmt in ["%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%d", "%Y%m%d"]:
        try:
            return datetime.datetime.strptime(string, fmt).date()
        except ValueError:
            continue
    raise ValueError(string)

def upper_keys(x):
    if isinstance(x, list):
        return [upper_keys(v) for v in x]
    elif isinstance(x, dict):
        return dict((k.upper(), upper_keys(v)) for k, v in x.items())
    else:
        return x

def check_key(data):
    try:
        return Client.objects.get(key=data["META_DATA"]['BROKER_KEY'])
    except:
        return None
