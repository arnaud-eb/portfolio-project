from django.shortcuts import render, get_object_or_404

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})

def jobdetail(request, job_id):
    jobdetail=get_object_or_404(Job, pk=job_id)
    return render(request,'jobs/detail.html',{'job':jobdetail})
