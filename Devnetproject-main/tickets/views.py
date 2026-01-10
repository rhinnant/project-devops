from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

    # Create ticket
    if request.method == 'POST' and 'create_ticket' in request.POST:
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
        'form': form,
        # ✅ Needed for assignment dropdown
        'users': User.objects.filter(is_staff=True)
    })


@login_required
def assign_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    # Only staff can assign tickets
    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        user_id = request.POST.get('assigned_to')
        ticket.assigned_to_id = user_id
        ticket.save()

    return redirect('ticket_list')


@login_required
def edit_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if (
        request.user != ticket.created_by and
        request.user != ticket.assigned_to and
        not request.user.is_staff
    ):
        raise PermissionDenied

    comments = ticket.comments.all().order_by('-created_at')

    if request.method == 'POST':
        # Add comment
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST, request.FILES)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.ticket = ticket
                comment.user = request.user
                comment.save()
                return redirect('edit_ticket', id=id)
        # Update ticket
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
