from django.db import models
from organizers.models import Organizer
from polls.models import Poll

# Create your models here.
class Candidate(models.Model):

    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    candidate_id = models.CharField(max_length=254, blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    department = models.CharField(max_length=254, blank=False)
    bio = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Candidates"

    def __str__(self) -> str:
        
        return self.first_name