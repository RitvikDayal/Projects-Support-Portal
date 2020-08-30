from django.shortcuts import render
from .models import *

def home(request):

    projects = Project.objects.all()

    context={
        'projects': projects,
    }

    return render(request, 'projects/index.html', context=context)

