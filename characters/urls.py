from rest_framework import routers

from characters.views import CharacterView, CharactersListView

router = routers.DefaultRouter()
router.register('characters', CharacterView)
router.register('characters-list', CharactersListView)