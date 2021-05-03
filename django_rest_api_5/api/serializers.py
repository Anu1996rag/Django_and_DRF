from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

        extra_kwargs = {
            "roll": {
                'validators': [UniqueValidator(queryset=Student.objects.all())]
            }
        }
