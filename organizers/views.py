from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from .models import Organizer
from polls.models import Poll
from candidates.models import Candidate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@permission_required('polls.add_poll', raise_exception=True)
def dashboard(request):

    user = request.user

    organizer = Organizer.objects.filter(user=user).first()

    organizer_polls = Poll.objects.filter(organizer=organizer)

    candidates = Candidate.objects.filter(organizer=organizer)

    context = {
        'all_polls': organizer_polls,
        'profile': organizer,
        'candidates': candidates,
        'user_account': user,
    }

    return render(request, 'organizers/dashboard.html', context)

def create_poll(request):

    if request.method == 'POST':

        user = request.user

        organizer = Organizer.objects.filter(user=user).first()

        seat = request.POST['seat']
        intro = request.POST['intro']
        organizer = organizer
        begin_date = request.POST['begin_date']
        end_date = request.POST['end_date']

        Poll.objects.create(
            seat=seat,
            intro=intro,
            organizer=organizer,
            begin_date=begin_date,
            end_date=end_date
        )

        messages.success(request, 'Poll has been created successfully.')

    return redirect('organizers-dashboard')

def register_candidate(request):

    if request.method == 'POST':

        user = request.user

        organizer = Organizer.objects.filter(user=user).first()

        organizer = organizer
        poll_id = request.POST['poll_id']
        poll = Poll.objects.get(id=poll_id)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        id_type = request.POST['id_type']
        personal_identification = request.POST['personal_id']
        image = request.FILES['image']
        country = request.POST['country']
        organization = request.POST['organization']

        Candidate.objects.create(
            organizer=organizer,
            poll=poll,
            first_name=first_name,
            last_name=last_name,
            email=email,
            id_type=id_type,
            personal_identification=personal_identification,
            image=image,
            country=country,
            organization=organization
        )

        messages.success(request, 'Candidate has been registered successfully.')

    return redirect('organizers-dashboard')

def view_poll(request, id):

    poll = Poll.objects.get(id=id)

    candidates = Candidate.objects.filter(poll=poll)

    context = {
        'this_poll': poll,
        'all_candidates': candidates,
    }

    return render(request, 'organizers/view_poll.html', context)

def view_candidate(request, id):

    candidate = Candidate.objects.get(id=id)

    context = {
        'this_candidate': candidate,
    }

    return render(request, 'organizers/view_candidate.html', context)

def update_poll(request, id):

    if request.method == 'POST':

        seat = request.POST['seat']
        intro = request.POST['intro']
        begin_date = request.POST['begin_date']
        end_date = request.POST['end_date']

        poll = Poll.objects.get(id=id)

        poll.seat = seat
        poll.intro = intro
        poll.begin_date = begin_date
        poll.end_date = end_date

        poll.save()

        messages.success(request, 'Poll has been updated successfully.')

    poll = Poll.objects.get(id=id)

    candidates = Candidate.objects.filter(poll=poll)

    context = {
        'this_poll': poll,
        'all_candidates': candidates,
    }

    return render(request, 'organizers/view_poll.html', context)

def close_poll(request, id):

    open = False

    poll = Poll.objects.get(id=id)

    poll.open = open

    poll.save()

    messages.success(request, 'Poll has been closed.')

    poll = Poll.objects.get(id=id)

    candidates = Candidate.objects.filter(poll=poll)

    context = {
        'this_poll': poll,
        'all_candidates': candidates,
    }

    return render(request, 'organizers/view_poll.html', context)

def delete_poll(request, id):

    poll = Poll.objects.get(id=id)

    poll.delete()

    messages.success(request, 'Poll has been deleted successfully.')

    return redirect('organizers-dashboard')

def update_candidate(request, id):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        id_type = request.POST['id_type']
        personal_identification = request.POST['personal_id']
        image = request.FILES['image']
        country = request.POST['country']
        organization = request.POST['organization']

        candidate = Candidate.objects.get(id=id)

        candidate.first_name = first_name
        candidate.last_name = last_name
        candidate.email = email
        candidate.id_type = id_type
        candidate.personal_identification = personal_identification
        candidate.image = image
        candidate.country = country
        candidate.organization = organization

        candidate.save()

        messages.success(request, 'Candidate record has been updated successfully.')

    candidate = Candidate.objects.get(id=id)

    context = {
        'this_candidate': candidate,
    }

    return render(request, 'organizers/view_candidate.html', context)

def delete_candidate(request, id):

    candidate = Candidate.objects.get(id=id)

    candidate.delete()

    messages.success(request, 'Candidate record has been deleted successfully.')

    return redirect('organizers-dashboard')

def update_profile(request, id):

    if request.method == 'POST':

        id_type = request.POST['id_type']
        personal_identification = request.POST['personal_id']
        phone = request.POST['phone']
        country = request.POST['country']
        sector = request.POST['sector']
        organization = request.POST['organization']
        organization_position = request.POST['organization_position']
        organization_email = request.POST['organization_email']
        organization_phone = request.POST['organization_phone']

        organizer = Organizer.objects.get(id=id)

        organizer.id_type = id_type
        organizer.personal_identification = personal_identification
        organizer.phone = phone
        organizer.country = country
        organizer.sector = sector
        organizer.organization = organization
        organizer.organization_position = organization_position
        organizer.organization_email = organization_email
        organizer.organization_phone = organization_phone

        organizer.save()

        messages.success(request, 'Your profile has been updated successfully.')

    return redirect('organizers-dashboard')

def delete_profile(request, id):

    profile = Organizer.objects.get(id=id)

    profile.delete()

    user = request.user

    user_id = user.id

    logout(request)

    account = User.objects.get(id=user_id)

    account.delete()

    messages.success(request, 'Your profile has been deleted successfully.')

    return redirect('home-page')
