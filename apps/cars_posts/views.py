from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import CarsPosts
from .serializers import CarsPostsSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.helpers.paginations import StandardPaginationSet
from apps.cars_posts.filters import CarsFilters
from django_filters import rest_framework as filters

class CarsPostsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = CarsPosts.objects.all()
    serializer_class = CarsPostsSerializer
    # permission_classes = [IsAuthenticated]

    # pagination
    pagination_class = StandardPaginationSet

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarsFilters

    search_fields = ['description']
    ordering_fields = ['created_at', 'price']

    def get_permissions(self):
        if self.action in ['create', 'partial_update', 'destroy', 'set_active']:
            return [IsAuthenticated()]
        return [AllowAny()]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not instance.is_active:
            return Response({"message": "Not found."}, status=404)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=204)

    @action(detail=True, methods=['patch'])
    def set_active(self, request, pk=None):
        instance = self.get_object()
        is_active = request.data.get('is_active', True)
        instance.is_active = is_active
        instance.save()
        return Response({'response': True, 'is_active': instance.is_active})
