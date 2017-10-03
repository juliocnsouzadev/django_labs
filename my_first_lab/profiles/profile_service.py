from profiles.models import Profile
from random import randint


def get_profile(id):
    try:
        return Profile.objects.get(id=int(id))
    except:
        return Profile()
