from django.shortcuts import render
from django.http import JsonResponse

def network(request):
    # Check if the request is asking for JSON data
    if request.GET.get('format') == 'json':
        # Return dynamic network topology data
        data = {
            "nodes": [
                {"data": {"id": "core", "label": "Core Router", "type": "router", "status": "up", "cpu": 35, "mem": 50}},
                {"data": {"id": "dist1", "label": "Distribution 1", "type": "switch", "status": "up", "cpu": 20, "mem": 30}},
                {"data": {"id": "dist2", "label": "Distribution 2", "type": "switch", "status": "down", "cpu": 90, "mem": 70}},
                {"data": {"id": "srv", "label": "App Server", "type": "server", "status": "up", "cpu": 50, "mem": 60}},
                {"data": {"id": "db", "label": "DB Server", "type": "server", "status": "down", "cpu": 95, "mem": 80}},
                {"data": {"id": "pc", "label": "User Workstation", "type": "host", "status": "up", "cpu": 10, "mem": 20}}
            ],
            "edges": [
                {"data": {"source": "core", "target": "dist1"}},
                {"data": {"source": "core", "target": "dist2"}},
                {"data": {"source": "dist1", "target": "srv"}},
                {"data": {"source": "dist2", "target": "db"}},
                {"data": {"source": "dist1", "target": "pc"}}
            ],
        }
        return JsonResponse(data)
    else:
        # Render your HTML page
        return render(request, "network/home.html")