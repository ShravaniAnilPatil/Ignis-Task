"""
URL configuration for joblisting project.
"""

from django.urls import path, include
from django.http import HttpResponse

# Simple view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the Job Listing API!")

urlpatterns = [
    path('', home_view),  # Root URL for homepage
    path('api/', include('jobs.urls')),  # Forward /api/ requests to jobs app
]
