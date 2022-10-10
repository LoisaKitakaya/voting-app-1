from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="organizers-dashboard"),
    path('create_poll/', views.create_poll, name="create-poll"),
    path('register_candidate', views.register_candidate, name="register-candidate"),
    path('dashboard/poll/<int:id>/', views.view_poll, name="view-poll"),
    path('dashboard/candidate/<int:id>/', views.view_candidate, name="view-candidate"),
    path('update_poll/<int:id>/', views.update_poll, name="update-poll"),
    path('delete_poll/<int:id>/', views.delete_poll, name="delete-poll"),
    path('close_poll/<int:id>/', views.close_poll, name="close-poll"),
    path('update_candidate/<int:id>/', views.update_candidate, name="update-candidate"),
    path('delete_candidate/<int:id>/', views.delete_candidate, name="delete-candidate"),
    path('update_profile/<int:id>/', views.update_profile, name="update-profile"),
    path('delete_profile/<int:id>/', views.delete_profile, name="delete-profile"),
]