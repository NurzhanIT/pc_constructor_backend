from rest_framework import serializers
# from pc_components.models import MonitorItemModel
# from pc_components.serializers import MonitorPcSerializer
from users_pc.models import UsersPcModel, UserMonitorModel, UserVideoCardModel


class UserMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMonitorModel
        fields = '__all__'


class VideoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVideoCardModel
        fields = '__all__'


class UserPcSerializer(serializers.ModelSerializer):
    usermonitormodel_set = UserMonitorSerializer(many=True, read_only=True)
    uservideocardmodel_set = VideoCardSerializer(many=True, read_only=True)

    class Meta:
        model = UsersPcModel
        fields = '__all__'
