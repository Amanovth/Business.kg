from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import CarsPosts, Media, Exterior, Interior, Safety, GeneralOptions, Pictures, CarPrices, User, Review
from drf_writable_nested import WritableNestedModelSerializer

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

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

class SafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = Safety
        fields = '__all__'

class GeneralOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOptions
        fields = '__all__'
        
class PicturesSerializer(serializers.ModelSerializer):
    pictures = VersatileImageFieldSerializer(
        sizes=[
            ('thumbnail', 'crop__100x100'),  
            ('small', 'crop__200x200'),      
            ('medium', 'crop__400x400'),     
            ('big', 'url')
        ]
    )
    class Meta:
        model = Pictures
        fields = ['pictures', ]
        
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrices
        fields = ['price', ]
        

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', '_avatar', 'phone']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        posted_count = CarsPosts.objects.filter(user=instance).count()
        comment_count = instance.reviews.count()
        avarage_rating = Review.get_average_rating(instance)
        representation['name'] = representation['name'] if representation['name'] else 'пользователь'
        representation['review_count'] = comment_count
        representation['avarage_rating'] = float(avarage_rating)
        representation['accommodation_count'] = posted_count
        return representation
    
class CarsPostsSerializer(serializers.ModelSerializer):
    # read only
    car_type_name = serializers.CharField(source="car_type.name", read_only=True)
    mark_name = serializers.CharField(source="mark.name", read_only=True)
    model_name = serializers.CharField(source="model.name", read_only=True)
    serie_name = serializers.CharField(source="serie.name", read_only=True)
    modification_name = serializers.CharField(source="modification.name", read_only=True)
    pictures = PicturesSerializer(many=True, read_only=True)
    user = UserInfoSerializer(read_only=True)
    prices = PriceSerializer(many=True, read_only=True)

    # additional
    likes = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = CarsPosts
        fields = '__all__'