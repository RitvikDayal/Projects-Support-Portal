from django.urls import path
from . import views

urlpatterns = [
    path('bugreport/<int:pk>/', views.bug_register, name='bugReport'),
]