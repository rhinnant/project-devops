from django.shortcuts import render, redirect
from .models import Scan, Vulnerability
from .parsers import parse_nessus

def upload_scan(request):
    if request.method == "POST":
        scan = Scan.objects.create(
            name=request.POST["name"],
            file=request.FILES["file"],
        )
        parse_nessus(scan.file.path, scan)
        return redirect("vulns")

    return render(request, "ACAS/home.html")


def vulns(request):
    vulns = Vulnerability.objects.all()
    return render(request, "ACAS/home.html", {"vulns": vulns})

