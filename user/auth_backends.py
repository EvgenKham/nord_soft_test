from django.contrib.auth.hashers import check_password
from user.models import Profile


class EmailAuthBackend(object):

    @staticmethod
    def authenticate(email=None, password=None):
        try:
            profile = Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return None

        if not check_password(password, profile.password):
            return None

        return profile

    @staticmethod
    def get_user(profile_id):
        try:
            return Profile.objects.get(pk=profile_id)
        except Profile.DoesNotExist:
            return None
