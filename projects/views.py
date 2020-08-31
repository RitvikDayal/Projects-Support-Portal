from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

def home(request):

    projects = Project.objects.all()

    context={
        'projects': projects,
    }

    return render(request, 'projects/index.html', context=context)

class ProjectDetailView(DetailView):
    model = Project