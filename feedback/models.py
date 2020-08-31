from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from projects.models import Project
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Feedback(models.Model):
    reported_by: models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feedback_title = models.CharField(max_length=150)
    review = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0),], 
                    help_text="Please Rate my project out of 5")
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return 'Project: {}\nFeedback: {}'.format(self.project.title, self.feedback_title)
    
    def get_absolute_url(self):
        return reverse("feedBack", kwargs={"pk": self.pk})
   
