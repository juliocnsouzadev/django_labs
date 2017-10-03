from django.shortcuts import render
from profiles.models import Profile
import profiles.profile_service as service

def index(request):
    return render(request, 'index.html')

def show(request, id):
    profile = service.get_profile(id)
    return render(request, 'profiles.html', {'profile': profile})