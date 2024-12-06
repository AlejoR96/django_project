from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# Create your views here.


def index(request):
    title = 'Django Course!!!'
    return render(request, 'index.html', {
        'title': title
    })


def hello(request, username):
    return HttpResponse("<h2> Hello %s </h2> " % username)


def about(request):
    username = 'Alejandro'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def task(request):
    # task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
