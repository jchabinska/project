from rest_framework import serializers
from .models import Osoba, Stanowisko


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