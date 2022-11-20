from django.contrib import admin
from .models import Voter, CurrentStudent

# Register your models here.
@admin.register(Voter)
class VoterAdminView(admin.ModelAdmin):

    model = Voter

    list_display = (
        'user',
        'student_id',
        'department',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )

@admin.register(CurrentStudent)
class CurrentStudentAdminView(admin.ModelAdmin):

    model = CurrentStudent

    list_display = (
        'first_name',
        'last_name',
        'student_id',
        'department',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )