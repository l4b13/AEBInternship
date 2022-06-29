from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import St_userSerializer
from web.models import St_user

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

@api_view(['GET'])
def getSt_users(request):
    st_users = St_user.objects.values('surname', 'name', 'patronymic', 'age', 'university', 'kurs', 'skills', 'is_accepted')
    serializer = St_userSerializer(st_users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addSt_user(request):
    serializer = St_userSerializer(data=request.data)
    if s