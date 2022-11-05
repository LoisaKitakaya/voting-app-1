from django.contrib import admin
from .models import Organizer

# Register your models here.
@admin.register(Organizer)
class OrganizerAdminView(admin.ModelAdmin):

    model = Organizer

    list_display = (
        'user',
        'personal_id',
        'department',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )