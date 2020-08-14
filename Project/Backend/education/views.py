from rest_framework import viewsets, status
from rest_framework.decorators import action
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

    @action(detail=True, methods=['post'])
    def registration(self, request, pk):
        course = self.get_object()
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        if not request.user.role == 2:
            return Response(data={"detail": "user must be student"},
                            status=status.HTTP_400_BAD_REQUEST)
        student = request.user
        if models.StudentCourse.objects.filter(course=course, student=student).exists():
            return Response(data={"detail": "student already have been registered in this course"},
                            status=status.HTTP_400_BAD_REQUEST)
        if student.credit < course.price:
            return Response(data={"detail": "student does't have enough credit"},
                            status=status.HTTP_400_BAD_REQUEST)
        student.credit -= course.price
        student.save()
        student_course_object = models.StudentCourse(course=course, student=student)
        student_course_object.save()
        return Response(data={'detail': 'registration is completed successfully'},
                        status=status.HTTP_200_OK)


class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = models.StudentCourse.objects.all()
    serializer_class = serializers.StudentCourseSerializer
    http_method_names = []
