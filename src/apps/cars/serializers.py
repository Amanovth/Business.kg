from rest_framework import serializers
from .models import (
    CarType, CarMark, CarModel, CarGeneration, CarSerie,
    CarModification, CarCharacteristic, CarCharacteristicValue,
    CarEquipment, CarOption, CarOptionValue
)


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ['id', 'name']


class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = ['id', 'name', 'img']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name']


class CarGenerationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarGeneration
        fields = ['id', 'name', 'img', 'year_begin', 'year_end']


class CarSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSerie
        fields = ['id', 'name']


class CarModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModification
        fields = ['id', 'name']


class CarCharacteristicValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='id_car_characteristic.name')

    class Meta:
        model = CarCharacteristicValue
        fields = ['name', 'value', 'unit']


class CarEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEquipment
        fields = ['id', 'name', 'id_car_modification', 'price_min', 'id_car_type', 'year']


class CarOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOption
        fields = ['id', 'name', 'id_parent', 'id_car_type']


class CarOptionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOptionValue
        fields = ['id', 'is_base', 'id_car_option', 'id_car_equipment', 'id_car_type']