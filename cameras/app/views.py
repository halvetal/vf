from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

class CameraFocusPlus(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['username']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/focus_plus/", data={})


class CameraFocusMinus(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/focus_minus/", data={})


class CameraFocusStop(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/focus_stop/", data={})


class CameraZoomUp(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/zoom_up/", data={})


class CameraZoomDown(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/zoom_down/", data={})


class CameraRight(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/right/", data={})


class CameraLeft(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/left/", data={})

class CameraUp(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/up/", data={})


class CameraDown(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/down/", data={})


class CameraStop(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/stop/", data={})


class CameraSetPreset(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/set_preset/", data={})


class CameraSelectPreset(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/select_preset/", data={})


class CameraGetPresets(APIView):
    def post(self, request):
        ip=request.data['ip']
        port_onvife=request.data['port_onvife']
        username=request.data['usernam']
        password=request.data['password']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if i['ip'] == ip:
                if i['username'] == username and i['password'] == password:
                    requests.post("http://127.0.0.1:5000/get_presets/", data={})
