from django.db import models
from organizers.models import Organizer
from polls.models import Poll

# Create your models here.
class Candidate(models.Model):

    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    id_type = models.CharField(max_length=254, blank=False)
    personal_identification = models.CharField(max_length=254, blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    country = models.CharField(max_length=254, blank=False)
    organization = models.CharField(max_length=254, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Candidates"

    def __str__(self) -> str:
        
        return self.first_name