from rest_framework import serializers
from .models import CarsPosts, Media, Exterior, Interior, Security, GeneralOptions

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class ExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = '__all__'

class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'

class GeneralOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOptions
        fields = '__all__'

class CarsPostsSerializer(serializers.ModelSerializer):
    # read only
    car_type_name = serializers.CharField(source="car_type.name", read_only=True)
    mark_name = serializers.CharField(source="mark.name", read_only=True)
    model_name = serializers.CharField(source="model.name", read_only=True)
    serie_name = serializers.CharField(source="serie.name", read_only=True)
    modification_name = serializers.CharField(source="modification.name", read_only=True)

    # nested
    exterior = ExteriorSerializer()
    interior = InteriorSerializer()
    media = MediaSerializer()
    security = SecuritySerializer()
    options = GeneralOptionsSerializer()

    class Meta:
        model = CarsPosts
        fields = (
            "id",
            "user",
            "car_type",
            "car_type_name",
            "mark",
            "mark_name",
            "model",
            "model_name",
            "year",
            "serie",
            "serie_name",
            "engine",
            "drive",
            "transmission",
            "modification",
            "modification_name",
            "steering_wheel",
            "video_url",
            "color",
            "condition",
            "mileage",
            "mileage_unit",
            "description",
            "availability",
            "customs_cleared",
            "registration",
            "other",
            "price",
            "currency",
            "exchange_possibility",
            "installment",

            # nested one to one
            "exterior",
            "interior",
            "media",
            "security",
            "options",
        )

    def create(self, validated_data):
        exterior_data = validated_data.pop('exterior')
        interior_data = validated_data.pop('interior')
        media_data = validated_data.pop('media')
        security_data = validated_data.pop('security')
        options_data = validated_data.pop('options')

        exterior = Exterior.objects.create(**exterior_data)
        interior = Interior.objects.create(**interior_data)
        media = Media.objects.create(**media_data)
        security = Security.objects.create(**security_data)
        options = GeneralOptions.objects.create(**options_data)

        # Create CarsPosts instance with related instances
        car_post = CarsPosts.objects.create(
            **validated_data,
            exterior=exterior,
            interior=interior,
            media=media,
            security=security,
            options=options
        )

        return car_post

    def update(self, instance, validated_data):
        # update for nested models

        exterior_data = validated_data.pop('exterior', None)
        interior_data = validated_data.pop('interior', None)
        media_data = validated_data.pop('media', None)
        security_data = validated_data.pop('security', None)
        options_data = validated_data.pop('options', None)

        if exterior_data:
            for attr, value in exterior_data.items():
                setattr(instance.exterior, attr, value)
            instance.exterior.save()

        if interior_data:
            for attr, value in interior_data.items():
                setattr(instance.interior, attr, value)
            instance.interior.save()

        if media_data:
            for attr, value in media_data.items():
                setattr(instance.media, attr, value)
            instance.media.save()

        if security_data:
            for attr, value in security_data.items():
                setattr(instance.security, attr, value)
            instance.security.save()

        if options_data:
            for attr, value in options_data.items():
                setattr(instance.options, attr, value)
            instance.options.save()

        # Update the rest of the fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance