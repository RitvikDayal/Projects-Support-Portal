from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
from bug_report.models import Bug
from feedback.models import Feedback

def home(request):

    projects = Project.objects.all()

    context={
        'projects': projects,
    }

    return render(request, 'projects/index.html', context=context)

def project_detail(request, pk):
    projects = Project.objects.all()
    bugs = Bug.objects.all()
    feedbacks = Feedback.objects.all()

    context ={
        'projects': projects,
        'bugs': bugs,
        'feedbacks': feedbacks,
        'project_id': pk
    }

    return render(request, 'projects/project_detail.html', context=context)