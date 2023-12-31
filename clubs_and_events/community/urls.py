from django.urls import path, include
from rest_framework.routers import DefaultRouter

from community.views import ClubViewSet, LabViewSet, EventViewSet, CommunityEventViewSet


router = DefaultRouter()
router.register('club', ClubViewSet)
router.register('event/community', CommunityEventViewSet)
router.register('event', EventViewSet)
router.register('lab', LabViewSet)

urlpatterns = [
    path('', include(router.urls))
]