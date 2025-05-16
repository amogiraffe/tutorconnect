from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TutorProfile

@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'subjects', 'hourly_rate')
    search_fields = ('user__username', 'subjects')