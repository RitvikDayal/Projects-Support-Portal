from django.urls import path
from . import views
from .views import ProjectDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]