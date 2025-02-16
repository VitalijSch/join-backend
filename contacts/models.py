from django.db import models
from django.core.validators import RegexValidator


class CustomContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            r'^[+]?[0-9]*$', message="Enter a valid phone number.")],
    )

    def __str__(self):
        return self.name
