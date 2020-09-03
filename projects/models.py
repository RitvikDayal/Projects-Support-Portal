from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User

class Project(models.Model):
    tag_choices = (
        ('personal', 'Personal'),
        ('freelance', 'Freelance'),
        ('professional', 'Professional')
    )

    title = models.CharField(max_length=100)
    project_image = models.ImageField(default='default_project.png', upload_to='project_pics')
    summary = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField()
    author = models.CharField(max_length=120)
    deploy_link = models.URLField(max_length=500, blank=True, null=True)
    tag = models.CharField(max_length=20,choices=tag_choices, default='personal')

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return 'Title: {}\nAuthor: {}'.format(self.title, self.author)
