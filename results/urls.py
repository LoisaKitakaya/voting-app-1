from django.urls import path
from . import views

urlpatterns = [
    path('poll_results/<int:id>/', views.poll_results, name="poll-results"),
    path('poll_report/<int:id>/', views.generate_report, name="generate-report"),
]