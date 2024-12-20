from django.urls import path
from .views import get_jobs, add_job

urlpatterns = [
    path('jobs/', get_jobs),
    path('jobs/add/', add_job),
]
