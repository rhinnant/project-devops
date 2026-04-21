from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Request

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'request/request_list.html', {'requests': requests})
