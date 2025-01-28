from rest_framework import serializers
from .models import Osoba, Stanowisko, Team
from .models import Person


class CustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        # Kod do tworzenia nowego obiektu
        pass

    def update(self, instance, validated_data):
        # Kod do aktualizacji obiektu
        pass

class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team  
        fields = '__all__' 