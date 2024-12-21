from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Job
import json

def get_jobs(request):
    jobs = list(Job.objects.values())
    return JsonResponse(jobs, safe=False) 

@csrf_exempt
def add_job(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            job = Job.objects.create(
                title=data.get('title'),
                company_name=data.get('company_name'),
                location=data.get('location'),
                employment_type=data.get('employment_type'),
                salary=data.get('salary'),
                details_url=data.get('details_url'),
                posted_date=data.get('posted_date'),
                modified_date=data.get('modified_date'),
                skills=data.get('skills'),
                location_type=data.get('location_type'),
                job_description=data.get('job_description')
            )
            
            return JsonResponse({'message': 'Job added successfully', 'job_id': job.id})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
