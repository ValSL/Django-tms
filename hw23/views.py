from django.shortcuts import render, reverse, redirect
from .serializers import CarSerializer
from .models import Car
from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status


# @api_view(['GET', 'POST', 'DELETE'])
# def api_car(request):
#     if request.method == 'GET' or request.method == 'DELETE':
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_car_detail(request, pk):
#     car = Car.objects.get(id=pk)
#     if request.method == 'GET':
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CarSerializer(car, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         car.delete()
#         return redirect(reverse_lazy(api_car))

class APICar(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICarDetail(APIView):
    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        if request.method == 'GET':
            serializer = CarSerializer(car)
            return Response(serializer.data)

    def put(self, request, pk):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = Car.objects.get(id=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
