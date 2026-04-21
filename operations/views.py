from django.shortcuts import render, get_object_or_404
from .models import Operation

def home(request):
    operations = Operation.objects.all()
    total_operations = operations.count()
    in_progress = operations.filter(status='In Progress').count()
    completed = operations.filter(status='Completed').count()

    progress_percent = int((in_progress / total_operations) * 100) if total_operations else 0
    completed_percent = int((completed / total_operations) * 100) if total_operations else 0

    context = {
        'operations': operations,
        'total_operations': total_operations,
        'in_progress': in_progress,
        'completed': completed,
        'progress_percent': progress_percent,
        'completed_percent': completed_percent,
    }
    return render(request, 'operations/home.html', context)


def operations_list(request):
    operations = Operation.objects.all()
    return render(request, "operations/operations_list.html", {"operations": operations})


def operations_detail(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    return render(request, "operations/operations_detail.html", {"operation": operation})
