import re

from rest_framework import serializers
from rest_framework.fields import empty, SkipField

from users.models import User
from users.validations import custom_validate_register


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'patronymic', 'password']


class UserRegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'last_name', 'first_name', 'patronymic', 'password']
        extra_kwargs = {
            'email': {'required': False,},
            'password': {'write_only': True, 'required': False,},
            'last_name':{'required': False,},
            'first_name':{'required': False,},
            'patronymic':{'required': False,},
        }

    def validate(self, data):
        custom_validate_register(data)
        return data



