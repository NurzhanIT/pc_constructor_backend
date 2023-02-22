from rest_framework import generics, permissions
from django.shortcuts import render

from users_pc.models import UsersPCModel, UserPCItemModel
from users_pc.serializers import UsersPCSerializer, UserPCItemSerializer


# Create your views here.


class UsersPCView(generics.ListCreateAPIView):
    # queryset = UsersPCModel.objects.all()
    serializer_class = UsersPCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UsersPCModel.objects.filter(user=user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UsersComponentView(generics.ListCreateAPIView):
    queryset = UserPCItemModel.objects.all()
    serializer_class = UserPCItemSerializer


