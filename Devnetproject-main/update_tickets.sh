#!/bin/bash
set -e

echo "🔧 Updating Django Ticket System..."

APP="tickets"
PROJECT="myproject"

# -----------------------------
# models.py
# -----------------------------
cat > $APP/models.py << 'EOF'
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_tickets'
    )

    assigned_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_tickets'
    )

    def __str__(self):
        return self.title


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    attachment = models.FileField(upload_to='ticket_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user}"
EOF

# -----------------------------
# forms.py
# -----------------------------
cat > $APP/forms.py << 'EOF'
from django import forms
from .models import Ticket, TicketComment
from django.contrib.auth.models import User

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ['comment', 'attachment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
EOF

# -----------------------------
# views.py
# -----------------------------
cat > $APP/views.py << 'EOF'
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Ticket, TicketComment
from .forms import TicketForm, CommentForm

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')

    search = request.GET.get('search')
    status = request.GET.get('status')
    priority = request.GET.get('priority')

    if search:
        tickets = tickets.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    if status and status != 'All':
        tickets = tickets.filter(status=status)

    if priority and priority != 'All':
        tickets = tickets.filter(priority=priority)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()

    return render(request, 'tickets/home.html', {
        'tickets': tickets,
        'form': form
    })


@login_required
def edit_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.user != ticket.created_by and request.user != ticket.assigned_to and not request.user.is_staff:
        raise PermissionDenied

    comments = ticket.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST, request.FILES)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.ticket = ticket
                comment.user = request.user
                comment.save()
                return redirect('edit_ticket', id=id)
        else:
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
        comment_form = CommentForm()

    return render(request, 'tickets/edit_ticket.html', {
        'ticket': ticket,
        'form': form,
        'comments': comments,
        'comment_form': comment_form
    })


@login_required
def delete_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')

    return render(request, 'tickets/delete_ticket.html', {'ticket': ticket})
EOF

# -----------------------------
# urls.py
# -----------------------------
cat > $APP/urls.py << 'EOF'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('edit/<int:id>/', views.edit_ticket, name='edit_ticket'),
    path('delete/<int:id>/', views.delete_ticket, name='delete_ticket'),
]
EOF

# -----------------------------
# Media settings
# -----------------------------
if ! grep -q "MEDIA_URL" $PROJECT/settings.py; then
cat >> $PROJECT/settings.py << 'EOF'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
EOF
fi

if ! grep -q "static(settings.MEDIA_URL" $PROJECT/urls.py; then
cat >> $PROJECT/urls.py << 'EOF'

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
EOF
fi

# -----------------------------
# Migrate
# -----------------------------
echo "🗄 Running migrations..."
python manage.py makemigrations tickets
python manage.py migrate

echo "✅ Ticket system updated successfully!"
echo "➡ Visit: http://127.0.0.1:8000/tickets/"

