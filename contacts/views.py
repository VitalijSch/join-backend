from .models import CustomContact
from .serializers import ContactSerializer
from rest_framework import generics

class CreateContactView(generics.CreateAPIView):
    queryset = CustomContact.objects.all()
    serializer_class = ContactSerializer