from rest_framework import viewsets
from .models import DeviceS7
from .serializer import DeviceS7Serializer

# Create your views here.
class DeviceS7View(viewsets.ModelViewSet):
    queryset = DeviceS7.objects.all()
    serializer_class = DeviceS7Serializer
