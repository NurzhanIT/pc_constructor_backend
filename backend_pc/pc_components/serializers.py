from rest_framework import serializers

from pc_components.models import PcComponentModel, DetailInfoModel


class DetailedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailInfoModel
        fields = '__all__'


class PcComponentSerializer(serializers.ModelSerializer):
    detailinfomodel = DetailedInfoSerializer()
    class Meta:
        model = PcComponentModel
        fields = '__all__'


    def create(self, validated_data):
        detail_info = validated_data.pop('detailinfomodel')
        component = PcComponentModel.objects.create(**validated_data)
        detail_info['component'] = component
        DetailInfoModel.objects.create(**detail_info)
        print(validated_data)
        return component
