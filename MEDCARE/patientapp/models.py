from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_history = models.TextField(blank=True)

class BloodSugarReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reading = models.IntegerField()

class nutritonalfacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()
    image=models.ImageField(upload_to='edu',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
class EducationalResource(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image=models.ImageField(upload_to='edu',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
