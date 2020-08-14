from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from education.models import Course, StudentCourse
from . import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        user_object = self.get_object()
        if request.user.role > 1:
            if not request.user.id == user_object.id:
                if request.user.is_anonymous:
                    return Response(data={"detail": "permission denied"},
                                    status=status.HTTP_400_BAD_REQUEST)
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        if not request.user.role == 1:
            return Response(data={"detail": "permission denied"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        try:
            username = request.data['username']
            all_user_objects = models.User.objects.all()
            all_usernames = [user_object.username for user_object in all_user_objects]
            if username in all_usernames:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            password = request.data['password']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            first_name = request.data['first_name']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            last_name = request.data['last_name']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = models.User(username=username, password=make_password(password),
                           first_name=first_name, last_name=last_name, role=2)
        user.save()
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        user_object = self.get_object()
        if request.user.role > 1:
            if not request.user.id == user_object.id:
                if request.user.is_anonymous:
                    return Response(data={"detail": "permission denied"},
                                    status=status.HTTP_400_BAD_REQUEST)
        username = user_object.username
        if 'username' in request.data:
            username = request.data['username']
            if not isinstance(username, str):
                return Response(data={'detail': 'username must be string'},
                                status=status.HTTP_400_BAD_REQUEST)
        is_password_sent, password = False, None
        if 'password' in request.data:
            is_password_sent = True
            password = request.data['password']
            if not isinstance(password, str):
                return Response(data={'detail': 'password must be string'},
                                status=status.HTTP_400_BAD_REQUEST)
        if 'first_name' in request.data:
            first_name = request.data['first_name']
            if not isinstance(first_name, str):
                return Response(data={'detail': 'first_name must be string'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            first_name = user_object.first_name
        if 'last_name' in request.data:
            last_name = request.data['last_name']
            if not isinstance(last_name, str):
                return Response(data={'detail': 'last_name must be string'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            last_name = user_object.last_name
        if 'gender' in request.data:
            gender = request.data['gender']
            if not (isinstance(gender, str) and gender in ['male', 'female']):
                return Response(data={'detail': 'gender must be male or female and have string type'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            gender = user_object.gender
        if 'phone_number' in request.data:
            phone_number = request.data['phone_number']
            if not isinstance(phone_number, str):
                return Response(data={'detail': 'phone_number must be string'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            phone_number = user_object.phone_number
        if 'credit' in request.data:
            credit = request.data['credit']
            if not isinstance(credit, float):
                return Response(data={'detail': 'credit must be float'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            credit = user_object.credit
        if 'date_of_birth' in request.data:
            date_of_birth = request.data['date_of_birth']
            if not isinstance(date_of_birth, str):
                return Response(data={'detail': 'date_of_birth must be str'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            date_of_birth = user_object.date_of_birth
        user_object.username = username
        if is_password_sent:
            user_object.password = make_password(password)
        user_object.first_name = first_name
        user_object.last_name = last_name
        user_object.gender = gender
        user_object.phone_number = phone_number
        user_object.credit = credit
        user_object.date_of_birth = date_of_birth
        user_object.save()
        return Response(data=serializers.UserSerializer(user_object).data,
                        status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def my_id(self, request):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'id': request.user.id}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def charge(self, request):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        if not request.user.role.id == 2:
            return Response(data={"detail": "user must be student"},
                            status=status.HTTP_400_BAD_REQUEST)
        if 'amount' in request.data:
            amount = request.data['amount']
            if not (isinstance(amount, int) or isinstance(amount, float)):
                return Response(data={'detail': 'amount must be int or float'},
                                status=status.HTTP_400_BAD_REQUEST)
            if amount <= 0:
                return Response(data={'detail': 'amount must be greater than 0'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "amount is necessary"},
                            status=status.HTTP_400_BAD_REQUEST)
        request.user.credit += amount
        request.user.save()
        return Response(data={'id': request.user.id}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def courses(self, request, pk):
        if request.user.is_anonymous:
            return Response(data={"detail": "user is anonymous"},
                            status=status.HTTP_400_BAD_REQUEST)
        response_data = {"courses": []}
        course_objects = [Course.objects.get(course=student_course_object.course) for student_course_object
                          in StudentCourse.objects.filter(student=models.User.objects.get(id=pk))]
        for course_object in course_objects:
            response_data["courses"].append({'course_id': course_object.id, 'course_name': course_object.name})
        return Response(data={'id': request.user.id}, status=status.HTTP_200_OK)
