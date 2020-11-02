from django.db import models
from django.contrib.auth.models import User

class Ghost(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True
    )
    description = models.TextField()