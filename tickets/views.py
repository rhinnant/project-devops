from django.shortcuts import render
from .models import Ticket


def tickets_page(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/home.html", {"tickets": tickets})


# ✅ NOW THIS RETURNS HTML (NOT JSON)
def ticket_api(request):
    tickets = Ticket.objects.all()

    data = {
        "tickets": tickets,
        "total": tickets.count(),
        "open": tickets.filter(status="OPEN").count(),
        "in_progress": tickets.filter(status="IN_PROGRESS").count(),
        "closed": tickets.filter(status="CLOSED").count(),
    }

    return render(request, "tickets/monitoring_dashboard.html", data)
