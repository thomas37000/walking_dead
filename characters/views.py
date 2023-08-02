from rest_framework import viewsets
from characters.models import Character, CharactersList
from characters.serializers import CharacterSerializer, CharactersListSerializer

class CharacterView(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_fields = ['is_alive']
    search_fields = ['name']

class CharactersListView(viewsets.ModelViewSet):
    queryset = CharactersList.objects.all()
    serializer_class = CharactersListSerializer