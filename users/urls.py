from rest_framework import routers

from users.views import UserView

router = routers.DefaultRouter()
router.register('user', UserView, basename='user')