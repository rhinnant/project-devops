from django.shortcuts import render

def accounts(request):
    return render(request, 'accounts/home.html')

