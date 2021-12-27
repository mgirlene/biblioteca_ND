from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from accounts.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'telefone', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['username'] = validated_data['email']
        return super(UsuarioSerializer, self).create(validated_data)