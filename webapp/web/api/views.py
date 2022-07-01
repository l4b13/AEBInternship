from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import St_userSerializer, UniversitySerializer, DegreeSerializer, StatusSerializer
from web.models import St_user, University, Degree, Status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

@api_view(['GET'])
def getUnivs(request):
    univs = University.objects.all()
    serializer = UniversitySerializer(univs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDegrees(request):
    degrees = Degree.objects.all()
    serializer = DegreeSerializer(degrees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSt_users(request):
    st_users = St_user.objects.values('surname', 'name', 'patronymic', 'age', 'university', 'current_degree', 'kurs', 'skills', 'is_accepted')
    serializer = St_userSerializer(st_users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addSt_user(request):
    serializer = St_userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getTest(request):
    someshit = St_user.objects.all()
    serializer = St_userSerializer(someshit, many=True)
    return Response(serializer.data)