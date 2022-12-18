from django.shortcuts import render
from rest_framework import generics

from pc_components.models import MonitorItemModel
from pc_components.serializers import MonitorPcSerializer


# Create your views here.


class MonitorView(generics.ListCreateAPIView):
    serializer_class = MonitorPcSerializer
    queryset = MonitorItemModel.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
