from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
