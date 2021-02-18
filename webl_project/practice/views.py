from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Problems, Submissions
from .forms import SubmissionsForms
#from uploads.run import Code
from .submit import Code
 
# Create your views here.
def problems(request):
    # query all problems
    all_problems = Problems.objects.all()
    return render(request, 'practice/problems.html', {'problems': all_problems})

def oneProblem(request, pk):
    problem = Problems.objects.get(id=pk)
    # create a dictionary and add the problem query
    # if the user is logged in, add the form in the dictionary as well
    context = {
        'problem':problem
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SubmissionsForms(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.problem = problem
                post.save()
                print(request.FILES)
                print(post.code.name)
                
                # now run the code against test cases
                # send the code name in the class below
                # send also the problem name
                coder = Code(post.code.name, problem.title)
                result = coder.check()
                return HttpResponse(result)
                #return redirect('users-dashboard')
                # run the code against test cases    
        else:
            form = SubmissionsForms()
        context['form'] = form    
    return render(request, 'practice/index.html', context)

"""
def uploadFile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SubmissionsForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, f'File Upload!')
                return redirect('users-dashboard')
        else:
            form = SubmissionsForms()
        return render(request, 'practice/upload.html', {'form':form})
    else:
        messages.success(request, 'You need to login in first')
        return redirect('users')
"""