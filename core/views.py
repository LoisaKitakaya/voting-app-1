from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from voters.models import Voter
from organizers.models import Organizer
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, 'core/landing_page.html')

def register_organizer(request):

    if request.method == 'POST':

        user = request.user
        id_type = request.POST['id_type']
        personal_identification = request.POST['personal_id']
        phone = request.POST['phone']
        country = request.POST['country']
        sector = request.POST['sector']
        organization = request.POST['organization']
        organization_position = request.POST['organization_position']
        organization_email = request.POST['organization_email']
        organization_phone = request.POST['organization_phone']

        Organizer.objects.create(
            user=user,
            id_type=id_type,
            personal_identification=personal_identification,
            phone=phone,
            country=country,
            sector=sector,
            organization=organization,
            organization_position=organization_position,
            organization_email=organization_email,
            organization_phone=organization_phone,
        )

        messages.success(request, 'Your organizer profile has been created.')

        return redirect('home-page')

    return render(request, 'core/register_organizer.html')

def register_voter(request):

    if request.method == 'POST':

        user = request.user
        id_type = request.POST['id_type']
        personal_identification = request.POST['personal_id']
        country = request.POST['country']
        organization = request.POST['organization']

        Voter.objects.create(
            user=user,
            id_type=id_type,
            personal_identification=personal_identification,
            country=country,
            organization=organization,
        )

        messages.success(request, 'Your voter profile has been created.')

        return redirect('home-page')

    return render(request, 'core/register_voter.html')

def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            messages.success(request, 'Logged in successfully!')

            user_type = request.user

            is_organizer = Organizer.objects.filter(user=user_type).first()

            is_voter = Voter.objects.filter(user=user_type)

            if is_organizer:

                return redirect('organizers-dashboard')

            if is_voter:

                return redirect('voters-dashboard')

        else:

            messages.error(request, 'You have entered a wrong username or password.')

    return render(request, 'core/login.html')

def signup_organizer(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user_already_exists = User.objects.filter(email=email).first()

        if not user_already_exists:

            if password1 == password2:

                User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )

                new_user = User.objects.get(email=email)

                new_user.set_password(password1)

                new_user.save()

                user = authenticate(request, username=username, password=password1)

                if user is not None:

                    login(request, user)

                messages.success(request, 'Your user account has been created. Logged in successfully!')

                return redirect('register-organizer')

            else:

                messages.error(request, 'Passwords did not match')

        else:

            messages.error(request, 'A user with the provided credentials already exists.')

    return render(request, 'core/signup.html')

def signup_voter(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user_already_exists = User.objects.filter(email=email).first()

        if not user_already_exists:

            if password1 == password2:

                User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )

                new_user = User.objects.get(email=email)

                new_user.set_password(password1)

                new_user.save()

                user = authenticate(request, username=username, password=password1)

                if user is not None:

                    login(request, user)

                messages.success(request, 'Your user account has been created. Logged in successfully!')

                return redirect('register-voter')

            else:

                messages.error(request, 'Passwords did not match')

        else:

            messages.error(request, 'A user with the provided credentials already exists.')

    return render(request, 'core/signup.html')

def logout_user(request):

    logout(request)

    return redirect('home-page')