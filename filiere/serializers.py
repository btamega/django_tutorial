from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from filiere.models import Filiere
from filiere.models import Etablissement

class FiliereSerializer(serializers.ModelSerializer):
    class Meta :
        model = Filiere
        fields = '__all__'

class EtablissementSerializer(serializers.ModelSerializer):
    class Meta :
        model = Etablissement
        fields = '__all__'