from rest_framework import serializers

from pc_components.serializers import PcComponentSerializer
from users_pc.models import UsersPCModel, UserPCItemModel


class UserPCItemSerializer(serializers.ModelSerializer):
    # components = PcComponentSerializer(read_only=True)
    class Meta:
        model = UserPCItemModel
        fields = '__all__'


class UsersPCSerializer(serializers.ModelSerializer):
    userpcitemmodel_set = UserPCItemSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = UsersPCModel
        fields = '__all__'

    #
    # def create(self, validated_data):
    #     pc_item = validated_data.pop('pc_item')
    #     request = self.context.get('request')
    #     print(self)
    #     user = request.user
    #     pc = UsersPCModel.objects.create(**validated_data, user=user)
    #     pc_item['pc'] = pc
    #     component = self.context['view'].kwargs.get('pk')
    #     pc_item['component'] = component
    #     UserPCItemModel.objects.create(**pc_item)
    #     print(validated_data)
    #     return component
