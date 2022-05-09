from functools import partial
from django.shortcuts import render
from .models import Customer
from rest_framework.views import APIView
from app1.serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CustomerDetails(APIView):
    def get (self, request):
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class CustomerInfo(APIView):

    def get(self, request, id):
        try:
             cust = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {'msg': 'Record Does Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        serializer = CustomerSerializer(cust)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            cust = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {'msg':'Record Does Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(cust, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            cust = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            msg = {'msg':'Record Does Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        cust.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

