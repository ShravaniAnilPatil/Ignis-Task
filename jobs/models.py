from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50)
    salary = models.CharField(max_length=100, null=True, blank=True)
    details_url = models.URLField()
    posted_date = models.DateField()

    def __str__(self):
        return self.title
