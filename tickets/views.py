from django.shortcuts import render
from django.http import JsonResponse
from .models import Ticket


# ----------------------------
# HTML DASHBOARD PAGE
# ----------------------------
def tickets_page(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets/home.html", {"tickets": tickets})


# ----------------------------
# HTML DASHBOARD (METRICS PAGE)
# ----------------------------
def monitoring_dashboard(request):
    tickets = Ticket.objects.all()

    data = {
        "tickets": tickets,
        "total": tickets.count(),
        "open": tickets.filter(status="OPEN").count(),
        "in_progress": tickets.filter(status="IN_PROGRESS").count(),
        "closed": tickets.filter(status="CLOSED").count(),
    }

    return render(request, "tickets/monitoring_dashboard.html", data)


# ----------------------------
# REAL API (JSON RESPONSE)
# ----------------------------
def ticket_api(request):
    tickets = Ticket.objects.all()

    data = {
        "total": tickets.count(),
        "open": tickets.filter(status="OPEN").count(),
        "in_progress": tickets.filter(status="IN_PROGRESS").count(),
        "closed": tickets.filter(status="CLOSED").count(),
        "tickets": list(
            tickets.values("id", "title", "status", "created_at")
        ),
    }

    return JsonResponse(data)
