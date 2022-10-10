from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('register_organizer/', views.register_organizer, name="register-organizer"),
    path('register_voter/', views.register_voter, name="register-voter"),
    path('login/', views.login_user, name="login"),
    path('signup_organizer/', views.signup_organizer, name="signup-organizer"),
    path('signup_voter/', views.signup_voter, name="signup-voter"),
    path('logout/', views.logout_user, name="logout-user")
]