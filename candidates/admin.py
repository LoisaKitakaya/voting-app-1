from django.contrib import admin
from .models import Candidate

# Register your models here.
@admin.register(Candidate)
class CandidateAdminView(admin.ModelAdmin):

    model = Candidate

    list_display = (
        'first_name',
        'email',
        'organization',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )