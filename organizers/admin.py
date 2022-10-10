from django.contrib import admin
from .models import Organizer

# Register your models here.
@admin.register(Organizer)
class OrganizerAdminView(admin.ModelAdmin):

    model = Organizer

    list_display = (
        'user',
        'organization',
        'status',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )