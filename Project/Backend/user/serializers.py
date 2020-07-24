from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'gender',
                  'phone_number', 'credit', 'date_of_birth']
