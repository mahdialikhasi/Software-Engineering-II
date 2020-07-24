from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

user_router = DefaultRouter()
user_router.register('user', views.UserViewSet)


urlpatterns = [
    path('', include(user_router.urls)),
]
