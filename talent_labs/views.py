from django.shortcuts import render
from .forms import JobApplicationForm


# Create your views here.
def JobApplicationHandler(request):
    form = JobApplicationForm()
    context = {'form': form}
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "success": "Job Has been added successfully. Checkout using above buttton..."}
        return render(request, 'job_form.html', context)
    return render(request, 'job_form.html', context)
