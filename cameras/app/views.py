from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json
# from dotenv import load_dotenv
# import os
# load_dotenv()
# MEDIASERVER_IP = os.getenv("MEDIASERVER_IP")
MEDIASERVER_IP = 'http://82.148.16.205:8001'


#@login_required
class CameraApi(APIView):
    def post(self, request):
        id=request.data['id']
        type=request.data['type']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if str(i['id']) == str(id):
                data = {
                    "cam_ip": i['ip'],
                    "port": i['port_onvife'],
                    "username": i['username'],
                    "password": i['password'],
                }
                requests.post(f"""{MEDIASERVER_IP}/{type}""", json=data)
        return Response({'':''})

class PresetSetApi(APIView):
    def post(self,request):
        id = request.data['id']
        token = request.data['token']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if str(i['id']) == str(id):
                data = {
                        "cam_ip": i['ip'],
                        "port": i['port_onvife'],
                        "username": i['username'],
                        "password": i['password'],
                        "id": id,
                        "token": token
                    }
                response = requests.post(f"""{MEDIASERVER_IP}/set_preset""", json=data)
                if response.status_code == 200:
                    preset_new = Precet.objects.create(
                        number = token,
                        id_camera = id,
                        preset = 'preset'
                    )
        return Response({'': ''})

class PresetSelectApi(APIView):
    def post(self, request):
        id = request.data['id']
        token = request.data['token']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if str(i['id']) == str(id):
                data = {
                    "cam_ip": i['ip'],
                    "port": i['port_onvife'],
                    "username": i['username'],
                    "password": i['password'],
                    "token": token
                }
                response = requests.post(f"""{MEDIASERVER_IP}/set_preset""", json=data)
                if response.status_code == 200:
                    return Response({"select_preset":"ok"})
        return Response({'': ''})



class PresetGetApi(APIView):
    def post(self,request):
        id = request.data['id']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if str(i['id']) == str(id):
                data = {
                    "cam_ip": i['ip'],
                    "port": i['port_onvife'],
                    "username": i['username'],
                    "password": i['password'],
                    "id": id
                }
                response = requests.post(f"""{MEDIASERVER_IP}/get_preset""", json=data)
                if response.status_code == 200:
                    presets = list(Precet.objects.all().values())
                    all_presets = []
                    for y in presets:
                        if str(y['id_camera']) == str(id):
                            all_presets.append(y)
                            return Response({"presets": all_presets})
        return Response({'presets': 'kakaya-to oshibka'})


class PresetDeleteApi(APIView):
    def post(self,request):
        id = request.data['id']
        token = request.data['token']
        lst = list(Camera.objects.all().values())
        for i in lst:
            if str(i['id']) == str(id):
                data = {
                    "cam_ip": i['ip'],
                    "port": i['port_onvife'],
                    "username": i['username'],
                    "password": i['password'],
                    "id": id,
                    "token": token
                }
                response = requests.post(f"""{MEDIASERVER_IP}/delete_preset""", json=data)
                if response.status_code == 200:
                    try:
                        preset = Precet.objects.get(id=token)
                        preset.delete()
                        return Response({"":""})
                    except:
                        return Response({"delete_preset":"kakaya-to oshibka"})
        return Response({'': ''})


# class PresetApi(APIView):
#     def post(self, request):
#         id = request.data['id']
#         command = request.data['command']
#         token = request.data['token']
#         if command == 'set_preset':
#             lst = list(Camera.objects.all().values())
#             for i in lst:
#                 if str(i['id']) == str(id):
#                     data = {
#                         "cam_ip": i['ip'],
#                         "port": i['port_onvife'],
#                         "username": i['username'],
#                         "password": i['password'],
#                         "id": id,
#                         "token": token
#                     }
#                     requests.post(f"""{MEDIASERVER_IP}/set_preset""", json=data)
#             return Response({'':''})
#
#         if command == 'select_preset':
#             pass
#         if command == 'get_preset':
#             lst = list(Camera.objects.all().values())
#             for i in lst:
#                 if str(i['id']) == str(id):
#                     presets = list(Precet.objects.all().values())
#                     for y in presets:
#                         if str(y['id_camera']) == str(id):
#                             data = {
#                                 "cam_ip": i['ip'],
#                                 "port": i['port_onvife'],
#                                 "username": i['username'],
#                                 "password": i['password'],
#                                 "id": id
#                             }
#                             requests.post(f"""{MEDIASERVER_IP}/get_preset""", json=data)
#             return Response({'': ''})
#         if command == 'delete_preset':
#             lst = list(Camera.objects.all().values())
#             for i in lst:
#                 if str(i['id']) == str(id):
#                     data = {
#                         "cam_ip": i['ip'],
#                         "port": i['port_onvife'],
#                         "username": i['username'],
#                         "password": i['password'],
#                         "id": id,
#                         "token": token
#                     }
#                     requests.post(f"""{MEDIASERVER_IP}/delete_preset""", json=data)
#             return Response({'': ''})
#         return Response({'': ''})
#
#
#
#
#
# class CamerasPost(APIView):
#     def get(self, request):
#         lst = Camera.objects.all().values()
#         return Response({'cameras': list(lst)})
#
#
#  # @login_required
#  # class CameraFocusPlus(APIView):
#  #     def post(self, request):
#  #         ip=request.data['ip']
#  #         port_onvife=request.data['port_onvife']
#  #         username=request.data['username']
#  #         password=request.data['password']
#  #         lst = list(Camera.objects.all().values())
#  #         data = {
# #             "ip": ip,
# #             "port_onvife": port_onvife,
# #             "user": username,
# #             "paassword": password,
# #             "type": "focus_plus"
# #         }
# #         for i in lst:
# #             if i['ip'] == ip:
# #                 if i['username'] == username and i['password'] == password:
# #                     requests.post(MEDIASERVER_IP, data=data)
# #
# #
# # @login_required
# # class CameraFocusMinus(APIView):
# #     def post(self, request):
# #         ip=request.data['ip']
# #         port_onvife=request.data['port_onvife']
# #         username=request.data['usernam']
# #         password=request.data['password']
# #         lst = list(Camera.objects.all().values())
# #         data = {
# #             "ip": ip,
# #             "port_onvife": port_onvife,
# #             "user": username,
# #             "paassword": password,
# #             "type": "focus_minus"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraFocusStop(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "focus_stop"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraZoomUp(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "zoom_up"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraZoomDown(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "zoom_down"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraRight(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "right"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraLeft(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "left"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraUp(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "up"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraDown(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "down"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraStop(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "stop"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraSetPreset(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "set_preset"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraSelectPreset(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "select_preset"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
#
#
# @login_required
# class CameraGetPresets(APIView):
#     def post(self, request):
#         ip=request.data['ip']
#         port_onvife=request.data['port_onvife']
#         username=request.data['usernam']
#         password=request.data['password']
#         lst = list(Camera.objects.all().values())
#         data = {
#             "ip": ip,
#             "port_onvife": port_onvife,
#             "user": username,
#             "paassword": password,
#             "type": "get_presets"
#         }
#         for i in lst:
#             if i['ip'] == ip:
#                 if i['username'] == username and i['password'] == password:
#                     requests.post(MEDIASERVER_IP, data=data)
