from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import SLA

def home(request):
    sla_count = SLA.objects.count()
    breached = SLA.objects.filter(status='BREACHED').count()
    on_track = SLA.objects.filter(status='ON_TRACK').count()

    return render(request, 'sla/home.html', {
        'sla_count': sla_count,
        'breached': breached,
        'on_track': on_track
    })


def sla_list(request):
    slas = SLA.objects.all().order_by('-start_time')
    return render(request, 'sla/sla_list.html', {'slas': slas})


def sla_detail(request, pk):
    sla = get_object_or_404(SLA, pk=pk)
    return render(request, 'sla/sla_detail.html', {'sla': sla})
