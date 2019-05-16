from django.shortcuts import render
from django.http import HttpResponse
import requests
from hl7parser.director import call_hl7_director

# Create your views here.
def getRequest(x):
    response = requests.get('https://api.myjson.com/bins/xgql6', verify=False)
    data = response.json()
    print(call_hl7_director(data).children)
    return HttpResponse("")