from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from polls.models import Poll
from candidates.models import Candidate
from django.contrib.auth.models import User
from .models import Voter
from votes.models import Vote
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
@permission_required('voters.add_voter', raise_exception=True)
def dashboard(request):

    user = request.user

    voter = Voter.objects.filter(user=user).first()

    polls = Poll.objects.all()

    context = {
        'all_polls': polls,
        'profile': voter,
        'user_account': user,
    }

    return render(request, 'voters/dashboard.html', context)

def update_profile(request, id):

    if request.method == 'POST':

        personal_id = request.POST['personal_id']
        department = request.POST['department']

        profile = Voter.objects.get(id=id)

        profile.personal_id = personal_id
        profile.department = department

        profile.save()

        messages.success(request, 'Your voter profile has been updated.')

    return redirect('voters-dashboard')

def delete_profile(request, id):

    profile = Voter.objects.get(id=id)

    profile.delete()

    user = request.user

    user_id = user.id

    logout(request)

    account = User.objects.get(id=user_id)

    account.delete()

    messages.success(request, 'Your profile has been deleted successfully.')

    return redirect('home-page')

def view_poll(request, id):

    poll = Poll.objects.get(id=id)

    candidates = Candidate.objects.filter(poll=poll)

    context = {
        'this_poll': poll,
        'all_candidates': candidates,
    }

    return render(request, 'voters/view_poll.html', context)

def view_candidate(request, id):

    candidate = Candidate.objects.get(id=id)

    context = {
        'this_candidate': candidate,
    }

    return render(request, 'voters/view_candidate.html', context)

def make_vote(request, id):

    if request.method == 'POST':

        user = request.user

        poll = Poll.objects.get(id=id)

        voter = Voter.objects.filter(user=user).first()

        has_voted = Vote.objects.filter(voter=voter, poll=poll).first()

        if has_voted:

            messages.error(request, 'You have already voted on this poll!')

            return redirect('voters-dashboard')

        poll = request.POST['poll_id']
        candidate = request.POST['candidate_id']

        v_poll = Poll.objects.get(id=poll)
        v_candidate = Candidate.objects.get(id=candidate)

        Vote.objects.create(
            poll=v_poll,
            candidate=v_candidate,
            voter=voter
        )

        messages.success(request, 'Your vote has been cast. You may view the results.')

    return redirect('voters-dashboard')