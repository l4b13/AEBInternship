import os
import subprocess
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import aSt_userSerializer, gSt_userSerializer, UniversitySerializer, DegreeSerializer
from web.models import St_user, University, Degree

# from .forms import VenueForm, EventForm, EventFormAdmin

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # '/api/token',
        # '/api/token/refresh',
        'get_st_users/',
        'add_st_user/',
        'get_univs/',
        'get_degrees/',
        'get_insts/',
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
def getSt_users(requestm, id=1):
    st_users = St_user.objects.filter(is_accepted='A')
    serializer = gSt_userSerializer(st_users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addSt_user(request):
    serializer = aSt_userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def some_view(request):
    return

def edit(request):
    return