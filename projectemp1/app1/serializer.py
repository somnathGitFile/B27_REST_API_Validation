import email
from wsgiref.validate import validator
from .models import Employee
from rest_framework import serializers

def multiple_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('salarary should be multiple of 1000')

class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators = [multiple_of_1000,])
    email = serializers.EmailField()
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_esal(self, value):
        if value < 10000:
            raise serializers.ValidationError('Salary should be grater than 10000 ')
        return value

    def validate(self, data):
        email = data.get("email")
        if email.endswith("gmail.com") != True:
            raise serializers.ValidationError('Domain name should be gmail.com')
        return data

        