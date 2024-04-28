# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Student
# from .serializer import StudentSerializer

# @api_view(['GET','POST'])
# def StudentViewList(request):
#     if request.method == 'GET':
#         student=Student.odject.all()
#         studentSerializer=StudentSerializer(student, many=True)
#         return Response(studentSerializer.data)
    
#     elif request.method == 'POST':
#         studentSerializer=StudentSerializer(data=request.data)
#         if studentSerializer.is_valid():
#             studentSerializer.save()
#             return Response(studentSerializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(studentSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['GET','PUT','DELETE'])
# def StudentDetailList(request,pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         studentSerializer=StudentSerializer(student)
#         return Response(studentSerializer.data)
    
#     elif request.method =='PUT':
#         studentSerializer=StudentSerializer(student , data=request.data)
#         if studentSerializer.is_valid():
#             studentSerializer.save()
#             return Response(studentSerializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(studentSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method =='DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer

@api_view(['GET', 'POST'])
def StudentViewList(request):
    if request.method == 'GET':
        student = Student.objects.all()
        studentSerializer = StudentSerializer(student, many=True)
        return Response(studentSerializer.data)
    elif request.method == 'POST':
        studentSerializer = StudentSerializer(data=request.data)
        if studentSerializer.is_valid():
            studentSerializer.save()
            return Response(studentSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(studentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailList(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        studentSerializer = StudentSerializer(student)
        return Response(studentSerializer.data)
    elif request.method == 'PUT':
        studentSerializer = StudentSerializer(student, data=request.data)
        if studentSerializer.is_valid():
            studentSerializer.save()
            return Response(studentSerializer.data, status=status.HTTP_200_OK)
        else:
            return Response(studentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
