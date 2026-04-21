from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Comment
from .forms import TaskForm, CommentForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()
    if request.method == 'POST' and 'add_task' in request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'task/task_list.html', {'tasks': tasks, 'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comment_form = CommentForm()
    if request.method == 'POST' and 'add_comment' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_detail', task_id=task.id)
    return render(request, 'task/task_detail.html', {'task': task, 'comment_form': comment_form})

