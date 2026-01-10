from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request):
    return render(request, 'UserProfile/view_profile.html')

@login_required
def edit_profile(request):
    # handle form data here
    return render(request, 'UserProfile/edit_profile.html')
