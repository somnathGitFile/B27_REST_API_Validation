from wsgiref.validate import validator
from .models import Customer
from rest_framework import serializers

def Multiple_of_1000(value):
    if value % 1000 !=0:
        raise serializers.ValidationError('customer bill should be in multiple of 1000')

class CustomerSerializer(serializers.Serializer):
    cid = serializers.IntegerField()
    cname= serializers.CharField(max_length=100)
    cadd = serializers.CharField(max_length=100)
    cmail = serializers.EmailField()
    cpay = serializers.FloatField(validators=[Multiple_of_1000])

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update (self,instance, validated_data):
        instance.eid = validated_data.get('cid', instance.cid)
        instance.ename = validated_data.get('cname', instance.cname)
        instance.eadd = validated_data.get('cadd', instance.cadd)
        instance.esal = validated_data.get('cmail', instance.cmail)
        instance.cpay = validated_data.get('cpay', instance.epay)

        instance.save()
        return instance

    def validate_cpay(self, value):
        if value < 10000:
            raise serializers.ValidationError('Customer bill should be grater than 10000 ')
        return value

    def validate(self, data):
        email = data.get("cmail")
        if email.endswith("gmail.com") != True:
            raise serializers.ValidationError('Domain name should be gmail.com')
        return data
