from django.shortcuts import render
from tickets.models import Ticket
from sla.models import SLA

def home(request):
    # Ticket status counts
    new_tickets_count = Ticket.objects.filter(status='New').count()
    in_progress_tickets_count = Ticket.objects.filter(status='In Progress').count()
    resolved_tickets_count = Ticket.objects.filter(status='Resolved').count()
    overdue_tickets_count = Ticket.objects.filter(status='Overdue').count()

    # SLA count
    sla_count = SLA.objects.count()

    # Progress calculations
    total_tickets = max(
        new_tickets_count + in_progress_tickets_count + resolved_tickets_count, 
        1
    )

    new_tickets_percent = round(new_tickets_count / total_tickets * 100)
    in_progress_tickets_percent = round(in_progress_tickets_count / total_tickets * 100)
    resolved_tickets_percent = round(resolved_tickets_count / total_tickets * 100)

    # Optional SLA progress (always 100 or calculate real metrics later)
    sla_percent = 100  

    # Recent tickets table
    recent_tickets = Ticket.objects.order_by('-id')[:5]

    # Send data to dashboard template
    context = {
        'new_tickets_count': new_tickets_count,
        'in_progress_tickets_count': in_progress_tickets_count,
        'resolved_tickets_count': resolved_tickets_count,
        'overdue_tickets_count': overdue_tickets_count,
        'sla_count': sla_count,

        'new_tickets_percent': new_tickets_percent,
        'in_progress_tickets_percent': in_progress_tickets_percent,
        'resolved_tickets_percent': resolved_tickets_percent,
        'sla_percent': sla_percent,

        'recent_tickets': recent_tickets,
    }

    return render(request, 'dashboard/home.html', context)

