from django.shortcuts import render, redirect
from django.contrib import messages
from projects.models import Project
from .forms import BugReportForm

def bug_register(request, pk):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.project = Project.objects.get(pk=int(pk))
            form.user = request.user
            print(form.project.id)
            form.save()
            messages.success(request, f'Thankyou for Reporting! We will review your issue and revert back soon,')
            return redirect('home')
        else:
            messages.warning(request, f'Please fill all the mandatory fields!')
    else:
        form = BugReportForm()
    context = {
        'form': form,
        'title': 'Register Bugs'
    }
    return render(request, 'bug_report/report.html', context=context)