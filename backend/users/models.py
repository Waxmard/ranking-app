from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    oauth_provider = models.CharField(max_length=255)
    oauth_id = models.CharField(max_length=255, unique=True)
    # created_at and updated_at are handled automatically

    def __str__(self):
        return self.email
