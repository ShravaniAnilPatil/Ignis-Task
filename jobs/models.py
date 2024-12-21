from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50)
    salary = models.CharField(max_length=100, null=True, blank=True)
    details_url = models.URLField(null=True, blank=True) 
    posted_date = models.DateField()
    modified_date = models.CharField(max_length=255, null=True, blank=True) 
    skills = models.TextField(null=True, blank=True)  
    location_type = models.CharField(max_length=50, null=True, blank=True)  
    job_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
