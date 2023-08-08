from rest_framework import views, viewsets, permissions, filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.settings import api_settings

from core.utils import filter_queryset
from user.models import User
from user.permissions import IsProfileOwner
from user.serializers import UserSerializer, LimitedUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ('get', 'put', 'patch', 'head', 'options')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'name', 'nickname')

    def get_queryset(self):
        queryset = self.queryset

        if self.request.user.is_authenticated:
            queryset = filter_queryset(queryset, self.request, target_param='is_active', is_foreign_key=False)
            queryset = filter_queryset(queryset, self.request, target_param='is_staff', is_foreign_key=False)
            queryset = filter_queryset(queryset, self.request, target_param='is_superuser', is_foreign_key=False)

        return queryset

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH'):
            return (permissions.IsAuthenticated(), IsProfileOwner())
        return tuple()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return UserSerializer
        return LimitedUserSerializer


class LoginAPIView(ObtainAuthToken):
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES