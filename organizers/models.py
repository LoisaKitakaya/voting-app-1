from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organizer(models.Model):

    DEPT_PROC = "Procurement and Logistics"
    DEPT_ECON = "Economics"
    DEPT_ACCF = "Accounting and Finance"
    DEPT_BIZN = "Business Administration"
    DEPT_ENGN = "Engineering"
    DEPT_COTE = "Construction and Textile"
    DEPT_ENTT = "Entrepreneurship and Technology"
    DEPT_LEMA = "Leadership and Management"

    SCHOOL_DEPARTMENTS = (
        (DEPT_PROC, 'dept of procurement and logistics'),
        (DEPT_ECON, 'dept of economics'),
        (DEPT_ACCF, 'dept of accounting and finance'),
        (DEPT_BIZN, 'dept of business administration'),
        (DEPT_ENGN, 'dept of engineering'),
        (DEPT_COTE, 'dept of construction and textile'),
        (DEPT_ENTT, 'dept of entrepreneurship and technology'),
        (DEPT_LEMA, 'dept of leadership and management'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer")
    staff_id = models.CharField(max_length=254, blank=False, unique=True)
    department = models.CharField(max_length=254, blank=False, choices=SCHOOL_DEPARTMENTS)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Organizers"

    def __str__(self) -> str:
        
        return self.user.username

class CurrentEmployee(models.Model):

    DEPT_PROC = "Procurement and Logistics"
    DEPT_ECON = "Economics"
    DEPT_ACCF = "Accounting and Finance"
    DEPT_BIZN = "Business Administration"
    DEPT_ENGN = "Engineering"
    DEPT_COTE = "Construction and Textile"
    DEPT_ENTT = "Entrepreneurship and Technology"
    DEPT_LEMA = "Leadership and Management"

    SCHOOL_DEPARTMENTS = (
        (DEPT_PROC, 'dept of procurement and logistics'),
        (DEPT_ECON, 'dept of economics'),
        (DEPT_ACCF, 'dept of accounting and finance'),
        (DEPT_BIZN, 'dept of business administration'),
        (DEPT_ENGN, 'dept of engineering'),
        (DEPT_COTE, 'dept of construction and textile'),
        (DEPT_ENTT, 'dept of entrepreneurship and technology'),
        (DEPT_LEMA, 'dept of leadership and management'),
    )

    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    staff_id = models.CharField(max_length=254, blank=False, unique=True)
    department = models.CharField(max_length=254, blank=False, choices=SCHOOL_DEPARTMENTS)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Current Employees"

    def __str__(self) -> str:
        
        return f'{self.first_name} {self.last_name}'