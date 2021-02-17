from django.shortcuts import render
from .models import Problems
# Create your views here.
def problems(request):
    # query all problems
    all_problems = Problems.objects.all()
    for i in Problems.objects.all():
        print(i.title)
    return render(request, 'practice/problems.html', {'problems': all_problems})

def oneProblem(request, pk):
    problem = Problems.objects.get(id=pk)
    return render(request, 'practice/index.html', {'problem': problem})