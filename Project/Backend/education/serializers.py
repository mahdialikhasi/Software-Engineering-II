from rest_framework import serializers

from . import models
from user.models import User


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=3))

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'teacher', 'time', 'address', 'content_titles', 'price']


class StudentCourseSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=2))
    course = serializers.PrimaryKeyRelatedField(many=False, queryset=models.Course.objects.all())

    class Meta:
        model = models.Course
        fields = ['id', 'student', 'course']
