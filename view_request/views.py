#from django.http import HttpResponse

#def request_view(request):
    #return HttpResponse("Hello from request_view")

from django.shortcuts import render

def request_view(request):
    return render(request, 'view_request/home.html')


