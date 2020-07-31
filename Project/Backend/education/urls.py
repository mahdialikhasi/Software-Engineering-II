from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

education_router = DefaultRouter()
education_router.register('course', views.CourseViewSet)
education_router.register('student-course', views.StudentCourseViewSet)


urlpatterns = [
    path('', include(education_router.urls)),
]
