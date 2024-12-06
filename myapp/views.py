from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# Create your views here.


def index(request):
    return HttpResponse("index page")


def hello(request, username):
    return HttpResponse("<h2> Hello %s </h2> " % username)


def about(request):
    return HttpResponse("About")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

# 1:32;00


def task(request, title):
    task = Task.objects.get(title=title)
   # task = get_object_or_404(Task, id=id)
    return HttpResponse('Task: %s' % task.title)
