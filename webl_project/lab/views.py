from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import LabProblems, Assignments, AssignmentSubmissions
from .forms import AssignmentSubmissionsForm
# Create your views here.


"""
    SOME CODES ARE DID NOT MAINTAIN THE
    DRY PRINCIPLE!
    BECAUSE I AM STILL GETTING USED TO DJANGO
    (I DONT EVEN KNOW HOW TO WRITE MIDDLEWARES!)
    YOU ARE FREE TO JUDGE ME AND I KNOW HOW
    INCOMPETENT I AM

"""



def labProblems(request):
    # query all lab problems
    if request.user.is_authenticated:
        if request.user.position == 'Teacher':
            lab_problems = LabProblems.objects.all()
            context = {
                'problems': lab_problems
            }
            return render(request, 'lab/problems.html', context)
        else:
            return redirect('practice-problems')
    else:
        return redirect('users-dashboard')

def labOneProblem(request, pk):
    problem = LabProblems.objects.get(id=pk)
    context = {
        'problem': problem
    }
    if request.method == 'POST':
        assignment = Assignments.objects.create(
            title=problem.title,
            description=problem.description,
            objective=problem.objective,
            task=problem.task,
            input_content=problem.input_content,
            output_content=problem.output_content
            )
        assignment.save()
        return render(request, 'lab/problems.html', context)
    else:
        return render(request, 'practice/index.html', context)

# for teachers to see the submissions
def submittedAssignments(request):
    # query all the submissions
    # if there are none, send an according message
    submissions = AssignmentSubmissions.objects.all()
    # checking if there any submissions at all
    if submissions:
        context = {
            'submissions':submissions
        }
        return render(request, 'lab/submissions.html', context)

# check single assignment
def oneSubmission(request, pk):
    # query the submission
    submission = AssignmentSubmissions.objects.get(id=pk)
    if submission:
        code = submission.code
        code = code.read().decode('utf-8')
        context = {
            'submission':submission,
            'code':code
        }
        return render(request, 'lab/singlesubmission.html', context)


def labAssignments(request):
    # these are for students
    # students can view and submit these
    # check if the user is authenticated, if not, redirect to login page
    # if it's a teacher, redirect to labs
    if request.user.is_authenticated:
        if request.user.position == 'Student':
            assignments = Assignments.objects.all()
            if assignments:
                context = {
                    'problems': assignments
            }
            else:
                context = {
                    'alert': "No assignments given yet."
                }
            return render(request, 'lab/assignment.html', context)
        else:
            return redirect('lab-labproblems')
    else:
        # redirect to login page
        messages.success(request, 'You need to login to first.')
        return redirect('user-login')

# viewing single assignment
def oneAssignment(request, pk):
    # check if the user is authenticated, if not redirect to login page
    # otherwise, check if the user is a student, let them access if it's so
    # otherwise redirect to teacher's lab
    if request.user.is_authenticated:
        if request.user.position == 'Student':
            # query assignment according to pk
            # if assignment doesn't exist, send a message
            # else, load the problem details and the form
            assignment = Assignments.objects.get(id=pk)
            if assignment:
                context = {
                    'problem':assignment
                }
                if request.method == 'POST':
                    form = AssignmentSubmissionsForm(request.POST, request.FILES)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.author = request.user
                        post.problem = assignment
                        post.save()
                        return HttpResponse('Assignment Submitted!')
                # if it's a GET request, create empty form
                else:
                    form = AssignmentSubmissionsForm()
                # adding form
                context['form'] = form
                return render(request, 'lab/submit.html', context)
            else:
                return HttpResponse('There is no such page. Sorry')
        else:
            # redirect to lab problems
            # because the user is not a student
            return redirect('lab-labproblems')
    else:
        # redirect to login
        messages.success(request, 'You need to login to first.')
        return redirect('user-login')