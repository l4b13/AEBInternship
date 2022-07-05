from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import aSt_userSerializer, gSt_userSerializer, UniversitySerializer, DegreeSerializer
from web.models import St_user, University, Degree

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # '/api/token',
        # '/api/token/refresh',
        'get_st_users/',
        'add_st_user/',
        'get_univs/',
        'get_degrees/',
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
    st_users = St_user.objects.select_related('university').select_related('current_degree').all()
    serializer = gSt_userSerializer(st_users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addSt_user(request):
    serializer = aSt_userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)