from rest_framework import viewsets
from .models import DeviceS7
from .serializer import DeviceS7Serializer
from django.shortcuts import render



# Create your views here.
class DeviceS7View(viewsets.ModelViewSet):
    queryset = DeviceS7.objects.all()
    serializer_class = DeviceS7Serializer

    
def get_last(request):
    queryset = DeviceS7.objects.last()
    serializer = DeviceS7Serializer(queryset)
    data = serializer.data
    return render(request, 'index.html', {'data': data})