from django.shortcuts import render, redirect
from .models import Submission
from .forms import SubmissionForm

def home(request):
    return render(request, 'myapp/home.html')

def submit_form(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submissions')
    else:
        form = SubmissionForm()
    return render(request, 'myapp/submit_form.html', {'form': form})

def submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'myapp/submissions.html', {'submissions': submissions})