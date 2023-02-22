from django.shortcuts import render
from rest_framework import generics

from pc_components.models import PcComponentModel, DetailInfoModel
from pc_components.serializers import PcComponentSerializer, DetailedInfoSerializer


# Create your views here.


class ComponentListView(generics.ListAPIView):
    serializer_class = PcComponentSerializer
    queryset = PcComponentModel.objects.all()

    # permission_classes = [permissions.IsAuthenticated]


class ComponentCreateView(generics.CreateAPIView):
    serializer_class = PcComponentSerializer
    queryset = PcComponentModel.objects.all()

    # permission_classes = [permissions.IsAuthenticated]


class ComponentDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PcComponentSerializer
    queryset = PcComponentModel.objects.all()

# class DetailedInfoView(generics.ListCreateAPIView):
#     serializer_class = DetailedInfoSerializer
#     queryset = DetailInfoModel.objects.all()
#
#
