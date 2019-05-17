from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from middleware.models import Device, TriggerEvent, Scope, Segment, Field
from middleware.serializers import DeviceSerializer
from hl7parser.director import call_hl7_director
from mllp.client import send_message


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
    data = JSONParser().parse(request)
    if is_request_valid(data):
        device= Device.objects.get(pk=data["meta_data"]["device"])
        print(call_hl7_director(data).children)
        # res = send_message(device.ip, int(device.port), call_hl7_director(data))

        # print(res)
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)  

def is_request_valid(data):
    if all(elem in data["meta_data"].keys() for elem in ["te","device","scope"]):
        if is_device_valid(data["meta_data"]["device"]) and is_capability_valid(data):
            return True
    return False

def is_device_valid(pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return False
    return True

def is_capability_valid(data):
    device = Device.objects.get(pk=data["meta_data"]["device"])
    te = TriggerEvent.objects.get(device=device, code=data["meta_data"]["te"])
    scope = Scope.objects.get(trigger_event=te, code=data["meta_data"]["scope"])
    segments = Segment.objects.filter(scope=scope)
    for segment in segments:
        if segment.name not in data["data"].keys():
            return False
        else:
            fields = Field.objects.filter(segment=segment)
            for field in fields:
                if field.name not in data["data"][segment.name]:
                    return False
    return True
