from django.http import Http404 # using later for status code 404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # using later on for status codes

from devices.models import Device
from devices.serializers import DeviceSerializer


class DeviceList(APIView):
    """
    List all devices.
    """
    def get(self, request, format=None):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
