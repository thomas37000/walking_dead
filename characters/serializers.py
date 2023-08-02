from rest_framework import serializers
from characters.models import Character, CharactersList

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
        
class CharactersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharactersList
        fields = "__all__"