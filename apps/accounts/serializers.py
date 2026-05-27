from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model  = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  

    def validate_email(self, value):
        value = value.lower().strip()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('A user with this email already exists')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()