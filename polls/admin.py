from django.contrib import admin
from .models import Poll

# Register your models here.
@admin.register(Poll)
class PollsAdminView(admin.ModelAdmin):

    model = Poll

    list_display = (
        'seat',
        'begin_date',
        'end_date',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )