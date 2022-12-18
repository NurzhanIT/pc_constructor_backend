from rest_framework import serializers

from pc_components.models import MonitorItemModel
from users_pc.serializers import UserPcSerializer


class MonitorPcSerializer(serializers.ModelSerializer):
    usersitemmodel_set = UserPcSerializer(many=True, read_only=True)
    class Meta:
        model = MonitorItemModel
        fields = '__all__'
