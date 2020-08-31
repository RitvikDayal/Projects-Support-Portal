from django.shortcuts import render, redirect
from django.contrib import messages
from projects.models import Project
from .forms import FeedbackForm

def bug_register(request, pk):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.project = Project.objects.get(pk=int(pk))
            form.user = request.user
            form.save()
            messages.success(request, f'Your feedback is very valuable to us. Thankyou!')
            return redirect('home')
        else:
            messages.warning(request, f'Please fill all the mandatory fields!')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedbackForm.html', {'form': form})