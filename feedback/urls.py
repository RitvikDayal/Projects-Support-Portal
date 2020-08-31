from django.urls import path
from . import views

urlpatterns = [
    path('feedback/<int:pk>/', views.bug_register, name='feedBack'),
]