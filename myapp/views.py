from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# Create your views here.


def index(request):
    return render(request, 'index.html')


def hello(request, username):
    return HttpResponse("<h2> Hello %s </h2> " % username)


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'project.html')

# 1:32;00


def task(request):
   # task = Task.objects.get(title=title)
   # task = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html')
