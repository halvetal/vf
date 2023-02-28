from django.urls import path
from .views import *

urlpatterns = [
    path('/', Camera.as_view())
#     path('focus_plus/', CameraFocusPlus.as_view()),
# path('focus_minus/', CameraFocusMinus.as_view()),
# path('focus_stop/', CameraFocusStop.as_view()),
# path('zoom_up/', CameraZoomUp.as_view()),
# path('zoom_down/', CameraZoomDown.as_view()),
# path('right/', CameraRight.as_view()),
# path('left/', CameraLeft.as_view()),
# path('up/', CameraUp.as_view()),
# path('down/', CameraDown.as_view()),
# path('stop/', CameraStop.as_view()),
# path('set_preset/', CameraSetPreset.as_view()),
# path('select_preset/', CameraSelectPreset.as_view()),
# path('get_presets/', CameraGetPresets.as_view()),


]
