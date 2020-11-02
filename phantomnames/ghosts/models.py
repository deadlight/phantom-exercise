from django.db import models
from django.contrib.auth.models import User

class Ghost(models.Model):
    name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, default='', null=True, blank=True)
    last_name = models.CharField(max_length=50, default='', null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True,
    )
    origin = models.CharField(max_length=50, default=None, null=True)
    description = models.TextField()