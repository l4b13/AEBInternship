from rest_framework.serializers import ModelSerializer
from web.models import St_user

class St_userSerializer(ModelSerializer):
    class Meta:
        model = St_user
        fields = '__all__'