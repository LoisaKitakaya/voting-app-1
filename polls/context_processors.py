from .models import Poll
from organizers.models import Organizer

def get_organizer_polls(request):

    user = request.user

    empty = []

    if user.is_authenticated:

        try:

            organizer = Organizer.objects.get(user=user)

        except:

            print("user is not associated with an organizer profile")

            return {
                'organizer_polls': empty
            }

        else:

            polls = Poll.objects.filter(organizer=organizer)

            return {
                'organizer_polls': polls
            }

    else:

        return {
            'organizer_polls': empty
        }