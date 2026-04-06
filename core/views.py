from django.shortcuts import render

# Create your views here.
# core/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Incident

class IncidentListView(ListView):
    model = Incident
    template_name = 'core/incident_list.html'

class IncidentDetailView(DetailView):
    model = Incident
    template_name = 'core/incident_detail.html'

class IncidentCreateView(CreateView):
    model = Incident
    fields = ['title', 'description', 'reported_by', 'status']
    template_name = 'core/incident_form.html'
    success_url = '/incidents/'

def home(request):
    return render(request, 'core/home.html')
# similarly for other models
