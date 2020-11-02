from django.contrib import admin
from .models import Ghost

@admin.register(Ghost)
class GhostAdmin(admin.ModelAdmin):
    pass