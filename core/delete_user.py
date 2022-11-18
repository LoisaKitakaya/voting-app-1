from django.contrib.auth.models import User

def delete_revoked_user(id):

    user_account = User.objects.get(id=id)

    user_account.delete()