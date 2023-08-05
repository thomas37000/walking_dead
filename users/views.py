from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.serialiserz import UserSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="This methods return all the users from the Django Walking Dead Admin",
        responses={200:UserSerializer},
    )
    def list(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)
