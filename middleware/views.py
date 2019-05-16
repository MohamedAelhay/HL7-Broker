from django.shortcuts import render
from django.http import HttpResponse
import requests
from hl7parser.director import call_hl7_director
from mllp.client import send_message

# Create your views here.
def getRequest(x):
    response = requests.get('https://api.myjson.com/bins/xgql6', verify=False)
    data = response.json()
    res = send_message('localhost', 6661, call_hl7_director(data))

    print(res)

    return HttpResponse(res)