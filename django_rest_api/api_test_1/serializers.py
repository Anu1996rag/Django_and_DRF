from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields to be displayed
        fields = ['id', 'name', 'roll', 'city']
        extra_kwargs = {
            'roll': {
                'validators': [UniqueValidator(queryset=Student.objects.all())]
            }
        }

    # Custom level validations must be below the level of Meta class and not inside the Meta class.
    # field level validation
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError("Seats Full..")
        return value

    def validate(self, data):
        city = data.get('city')
        if city == "bgm":
            raise serializers.ValidationError("City must not be bgm...")
        return data

# below is the implementation of serializers without using ModelSerializer class
# creating for one model object - single row of database table
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=50)
#
#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.roll = validated_data.get("roll", instance.roll)
#         instance.city = validated_data.get("city", instance.city)
#         instance.save()
#
#         return instance
#
#     # adding validation for roll
#     def validate_roll(self, value):
#         if value > 200:
#             raise serializers.ValidationError("Seats are full")
#         return value
#
#     # object level validation
#     def validate(self, data):
#         city = data.get("city")
#         if city.lower() == "bgm":
#             raise serializers.ValidationError("City must not be 'bgm'.")
#         return data
