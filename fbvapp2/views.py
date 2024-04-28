#import form django and restframework
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Schools
from .serializer import SchoolSerializer


#appling method on requests---------------------------------------------------,..


@api_view(['GET', 'POST'])
def SchoolListView(request):
    if request.method == 'GET':
        school = Schools.objects.all()
        schoolSerializer = SchoolSerializer(school, many=True)
        return Response(schoolSerializer.data)

    
    elif request.method == 'POST':
        schoolSerializer = SchoolSerializer(data=request.data)
        
        if schoolSerializer.is_valid():
            schoolSerializer.save()
            return Response(schoolSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(schoolSerializer.errors, status=status.HTTP_400_BAD_REQUEST)



# appling method by primary key --------------------------------------------------------,.....


@api_view(['GET', 'PUT', 'DELETE'])
def SchooldetailsView(request, pk):
    try:
        school = Schools.objects.get(pk=pk)
    except Schools.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        schoolSerializer = SchoolSerializer(school)
        return Response(schoolSerializer.data)
    elif request.method == 'PUT':
        schoolSerializer = SchoolSerializer(school, data=request.data)
        if schoolSerializer.is_valid():
            schoolSerializer.save()
            return Response(schoolSerializer.data)
        else:
            return Response(schoolSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    