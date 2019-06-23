from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def project_list(request):
    project_li = Project.objects.all()
    return render(request, 'projects.html', locals())

def project_detail(request, id):
    project = Project.objects.filter(id=id)
    return render(request, 'project_detail.html', locals())

