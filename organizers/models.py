from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organizer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer")
    staff_id = models.CharField(max_length=254, blank=False, unique=True)
    department = models.CharField(max_length=254, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Organizers"

    def __str__(self) -> str:
        
        return self.user.username

class CurrentEmployee(models.Model):

    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    staff_id = models.CharField(max_length=254, blank=False, unique=True)
    department = models.CharField(max_length=254, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Current Employees"

    def __str__(self) -> str:
        
        return f'{self.first_name} {self.last_name}'