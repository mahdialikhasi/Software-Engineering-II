from rest_framework import viewsets, status
from rest_framework.response import Response

from . import serializers, models


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(CourseViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(CourseViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        if request.user.role > 1:
            return Response(data={"detail": "permission denied"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(CourseViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        if request.user.role > 1:
            return Response(data={"detail": "permission denied"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(CourseViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        if request.user.role > 1:
            return Response(data={"detail": "permission denied"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(CourseViewSet, self).destroy(request, *args, **kwargs)


class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = models.StudentCourse.objects.all()
    serializer_class = serializers.StudentCourseSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
