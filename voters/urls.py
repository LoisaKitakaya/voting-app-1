from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="voters-dashboard"),
    path('update_profile/<int:id>/', views.update_profile, name="update-voter-profile"),
    path('delete_profile/<int:id>/', views.delete_profile, name="delete-voter-profile"),
    path('dashboard/poll/<int:id>/', views.view_poll, name="view-voter-poll"),
    path('dashboard/candidate/<int:id>/', views.view_candidate, name="view-voter-candidate"),
    path('make_vote/<int:id>/', views.make_vote, name="make-vote"),
]