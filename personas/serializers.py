from django.contrib.auth.models import User
from rest_framework import serializers
from personas.models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['url','nombre', 'apellido', 'cedula']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    persona = PersonaSerializer(source='persona_set.first', read_only=True, allow_null=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'persona']
