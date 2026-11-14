from rest_framework import serializers
from django.contrib.auth.models import User
from eventmaster.models import EventDb


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ["id","username","email","password"]
        read_only_fields = ["id"]
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDb
        fields = '__all__'
        read_only_fields = ['id','created_by','created_at','updated_at']