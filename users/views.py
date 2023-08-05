from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.serialiserz import UserSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)
