from rest_framework import serializers
from .models import CustomContact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomContact
        fields = ['name', 'email', 'phone_number']
