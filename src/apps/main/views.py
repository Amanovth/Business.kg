from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.main import models
from apps.main import serializers

# data
''' cars '''
from apps.cars_posts.models import CarsPosts
from apps.cars_posts.serializers import CarsPostsSerializer

''' houses '''
from apps.house.models import Property
from apps.house.serializers import PropertySerializer
from itertools import chain


class CommentView(viewsets.GenericViewSet):
    queryset = models.Comments.objects.all().order_by('-id')
    serializer_class = serializers.CommentSerializer

    @action(detail=False, methods=['post'])
    def create_comment(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "comment succes created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeViews(viewsets.GenericViewSet):
    def get_queryset(self):
        type = self.kwargs.get("type")
        if type == "car":
            return CarsPosts.objects.all()
        if type == "house":
            return Property.objects.all()
        return None

    @action(detail=True, methods=["get"], url_path='(?P<type>house|car)/set_like')
    def set_like(self, request, pk=None, type=None):
        instance = self.get_object()
        if instance is None:
            return Response({"error": "Invalid type"}, status=400)

        instance.likes.add(request.user)
        instance.save()
        return Response({"message": "Like added successfully"})

    @action(detail=True, methods=["get"], url_path='(?P<type>house|car)/remove_like')
    def remove_like(self, request, pk=None, type=None):
        instance = self.get_object()
        if instance is None:
            return Response({"error": "Invalid type"}, status=400)

        instance.likes.remove(request.user)
        instance.save()
        return Response({"message": "Like removed successfully"})

    @action(detail=False, methods=["get"], url_path="my_favorites")
    def my_favorites(self, request):
        user = request.user

        ''' cars data '''
        car_favorites = CarsPosts.objects.filter(likes=user)
        context = {'is_detail': False}
        cars_serializer = CarsPostsSerializer(car_favorites, many=True, context=context).data

        ''' house data '''
        house_favorites = Property.objects.filter(likes=user)
        house_serializer = PropertyListSerializer(house_favorites, many=True).data

        ''' using list comprehension for adding datatype '''
        cars_with_type = [{**car, 'object_type': 'car'} for car in cars_serializer]
        houses_with_type = [{**house, 'object_type': 'house'} for house in house_serializer]

        ''' merge all data and sorting with key "created_at" '''
        combined_data = sorted(
            chain(cars_with_type, houses_with_type),
            key=lambda obj: obj['created_at']
        )

        return Response({"data": combined_data})
