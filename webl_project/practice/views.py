from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Problems, Submissions
from .forms import SubmissionsForms
from .submit import Code
 
# Create your views here.
def problems(request):
    # query all problems
    all_problems = Problems.objects.all()
    return render(request, 'practice/labexp.html', {'problems': all_problems})

def oneProblem(request, pk):
    problem = Problems.objects.get(id=pk)
    # create a dictionary and add the problem query
    # if the user is logged in, add the form in the dictionary as well
    context = {
        'problem':problem
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            # take the submitted form
            # save the form in the db
            # add the user and problem (as they are the foreign keys)
            # create a "Code" instance and run the code
            # add the results to the "context" dictionary
            # redirect/reload this page
            
            ### THIS CHANGES ARE YET TO BE IMPLEMENTED!
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
                judgement = result[-1]
                result.pop()
                # receive the array
                # send the array in the context
                # the result will carry an array and
                context['test_results'] = result
                context['form'] = form
                context['judgement'] = judgement
                return render(request, 'practice/solve.html', context)
        else:
            form = SubmissionsForms()
        context['form'] = form    
    return render(request, 'practice/solve.html', context)

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