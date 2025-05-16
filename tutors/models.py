from django.db import models

# Create your models here.
from accounts.models import User

class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=200)  # e.g., "Math, Physics"
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.JSONField(default=dict)  # {"Monday": ["14:00", "16:00"]}

class Appointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_appointments')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_appointments')
    date_time = models.DateTimeField()
    duration = models.PositiveIntegerField()  # in minutes
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed')
    ])