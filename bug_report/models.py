from django.db import models
from projects.models import Project
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    bug_title = models.CharField(max_length=150)
    bug_description = models.TextField()
    screenshot = models.ImageField(blank=True, null=True, upload_to='Bug_Reports')
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return 'Project: {}\nBug: {}'.format(self.project.title, self.bug_title)
    
    # def get_absolute_url(self):
    #     return reverse("bug-detail", kwargs={"pk": self.pk})
   
