from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
MEDIASERVER_IP = os.getenv("MEDIASERVER_IP")


@login_required
class CameraFocusPlus(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['username']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "focus_plus"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraFocusMinus(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "focus_minus"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraFocusStop(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "focus_stop"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraZoomUp(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "zoom_up"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraZoomDown(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "zoom_down"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraRight(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "right"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraLeft(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "left"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraUp(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "up"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraDown(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "down"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraStop(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "stop"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraSetPreset(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "set_preset"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraSelectPreset(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "select_preset"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)


@login_required
class CameraGetPresets(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        data = {
            "ip": ip,
            "port_onvife": port_onvife,
            "user": username,
            "paassword": password,
            "type": "get_presets"
        }
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post(MEDIASERVER_IP, data=data)
