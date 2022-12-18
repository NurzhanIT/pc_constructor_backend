from django.shortcuts import render
from rest_framework import generics, permissions, mixins

from pc_components.models import MonitorItemModel
from users_pc.models import UsersPcModel, UserMonitorModel, UserVideoCardModel
from users_pc.serializers import UserPcSerializer, UserMonitorSerializer, VideoCardSerializer


# Create your views here.


class UserPcView(generics.ListCreateAPIView):
    serializer_class = UserPcSerializer
    queryset = UsersPcModel.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     user = self.request.user
    #     return UsersItemModel.objects.filter(user=user)

    # def perform_create(self, serializer):
    #     monitor_id = MonitorItemModel.objects.filter()
    #     serializer.save(user=self.request.user)


class UserPcDeleteView(generics.DestroyAPIView):
    serializer_class = UserPcSerializer
    queryset = UsersPcModel.objects.all()


class UserMonitorView(generics.ListCreateAPIView):
    queryset = UserMonitorModel.objects.all()
    serializer_class = UserMonitorSerializer


class UserMonitorDestroyView(generics.DestroyAPIView):
    queryset = UserMonitorModel.objects.all()
    serializer_class = UserMonitorSerializer


class VideoCardView(generics.ListCreateAPIView):
    queryset = UserVideoCardModel.objects.all()
    serializer_class = VideoCardSerializer


class VideoCardDeleteView(generics.DestroyAPIView):
    queryset = UserVideoCardModel.objects.all()
    serializer_class = VideoCardSerializer
