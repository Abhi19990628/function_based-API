from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course
from .serializer import CourseSerializer

@api_view(['GET','POST'])
def courseListView(resquest):
    if resquest.method == 'GET':
        course=Course.objects.all()
        courseSerializer=CourseSerializer(course , many=True)
        return Response(courseSerializer.data)
    
    
    elif resquest.method == 'POST':
        courseSerializer=CourseSerializer(data = resquest.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        
        return Response(courseSerializer.errors)
        
    
@api_view(['GET','PUT','DELETE'])
def courseDetailView(resquest, pk ):
    
    try:
        course=Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if resquest.method == 'GET':
        courseSerializer=CourseSerializer(course)
        return Response(courseSerializer.data)
    
    
    
    elif resquest.method == 'PUT':
        courseSerializer=CourseSerializer(course , data = resquest.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)
    
    elif resquest.method == 'DELETE':
        course.delete
        return Response(status=status.HTTP_400_BAD_REQUEST)