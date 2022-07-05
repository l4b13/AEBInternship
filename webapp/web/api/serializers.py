from rest_framework.serializers import ModelSerializer
from web.models import St_user, University, Status, Degree
from django.contrib.auth.models import User

class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class DegreeSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class St_userSerializer(ModelSerializer):
    class Meta:
        model = St_user
        fields = ('email','surname', 'name', 'patronymic', 'age', 'university', 'current_degree', 'kurs', 'skills', 'is_accepted')