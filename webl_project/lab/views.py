from django.shortcuts import render
from django.http import HttpResponse
from .models import LabProblems, Assignments
# Create your views here.

def labProblems(request):
    #return HttpResponse('<h1>Home</h1>')
    # query all lab problems
    lab_problems = LabProblems.objects.all()
    context = {
        'problems': lab_problems
    }
    return render(request, 'lab/problems.html', context)



def labOneProblem(request, pk):
    problem = LabProblems.objects.get(id=pk)
    context = {
        'problem': problem
    }
    if request.method == 'POST':
        assignment = Assignments.objects.create(problems=problem)
        assignment.save()
        return render(request, 'lab/problems.html', context)
    else:
        return render(request, 'practice/index.html', context)

def labAssignments(request):
    assignments = Assignments.objects.all()
    for i in assignments:
        print(i)
    context = {
        'problems': assignments
    }
    return render(request, 'lab/problems.html', context)