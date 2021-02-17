from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Problems, Submissions
from .forms import SubmissionsForms
# Create your views here.
def problems(request):
    # query all problems
    all_problems = Problems.objects.all()
    return render(request, 'practice/problems.html', {'problems': all_problems})

def oneProblem(request, pk):
    problem = Problems.objects.get(id=pk)
    return render(request, 'practice/index.html', {'problem': problem})


def uploadFile(request):
    if request.method == 'POST':
        form = SubmissionsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'File Upload!')
            return HttpResponse('File Uploaded!')
    else:
        form = SubmissionsForms()
    return render(request, 'practice/upload.html', {'form':form})