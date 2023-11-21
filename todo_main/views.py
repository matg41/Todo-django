#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('modified_at')

    compeleted_tasks = Task.objects.filter(is_completed=True)
    
    context = {
        "tasks": tasks,
        'compeleted_tasks': compeleted_tasks,
    }
    return render(request, 'home.html', context)