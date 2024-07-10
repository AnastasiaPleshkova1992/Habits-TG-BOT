from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """Haches the user's password"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
