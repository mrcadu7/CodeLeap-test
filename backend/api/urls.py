
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CareersViewSet


router = DefaultRouter()
router.register(r'careers', CareersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
