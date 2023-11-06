from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import paho.mqtt.client as mqtt
import json
from django.http import JsonResponse
from chat.mqtt import client as mqtt_client
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "chat/chat.html")

@csrf_exempt
def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})
