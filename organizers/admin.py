from django.contrib import admin
from .models import Organizer, CurrentEmployee

# Register your models here.
@admin.register(Organizer)
class OrganizerAdminView(admin.ModelAdmin):

    model = Organizer

    list_display = (
        'user',
        'staff_id',
        'department',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

@admin.register(CurrentEmployee)
class CurrentEmployeeAdminView(admin.ModelAdmin):

    model = CurrentEmployee

    list_display = (
        'first_name',
        'last_name',
        'staff_id',
        'department',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )