from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from web.models import St_user, University, Degree
from django.contrib.auth.models import User

class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class UnivNameSerilalizer(ModelSerializer):
    class Meta:
        model = University
        fields = ('uname',)

class DegreeSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class aSt_userSerializer(ModelSerializer):
    class Meta:
        model = St_user
        fields = '__all__'

class gSt_userSerializer(ModelSerializer):
    univ = serializers.CharField(source='university.uname')
    deg = serializers.CharField(source='current_degree.degree_name')

    class Meta:
        model = St_user
        fields = ('email','surname', 'name', 'patronymic', 'age', 'univ', 'deg', 'kurs', 'skills', 'is_accepted')