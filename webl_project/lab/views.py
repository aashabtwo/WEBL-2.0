from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

import os

from .models import LabProblems, Assignments, AssignmentSubmissions
from .forms import AssignmentSubmissionsForm
# Create your views here.


"""
    SOME CODES DID NOT MAINTAIN THE
    DRY PRINCIPLE!
    BECAUSE I AM STILL GETTING USED TO DJANGO
    (I DONT EVEN KNOW HOW TO WRITE MIDDLEWARES!)
    YOU ARE FREE TO JUDGE ME AND I KNOW HOW
    INCOMPETENT I AM

"""
path = os.getcwd()
parent_path = os.path.abspath(os.path.join(path, os.pardir))
assignment_submission_path = parent_path + '/webl_project/assignmentSubmissions/'


# theory
def theory(request):
    return render(request, 'lab/exp1.html')

# lab list
def list(request):
    return render(request, 'lab/lablist.html')
def pick(request):
    return render(request, 'lab/Clab.html')


# all problems
def labProblems(request):
    # query all lab problems
    accepted_submissions = AssignmentSubmissions.objects.filter(reviewed=True, approved=True)
    rejected_submissions = AssignmentSubmissions.objects.filter(reviewed=True, approved=False)
    if request.user.is_authenticated:
        if request.user.position == 'Teacher':
            lab_problems = LabProblems.objects.all()
            context = {
                'problems': lab_problems,
                'accepted': accepted_submissions,
                'rejected': rejected_submissions,
            }
            return render(request, 'lab/labexp.html', context)
        else:
            return redirect('practice-problems')
    else:
        return redirect('users-dashboard')

# checks one problem
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
        return render(request, 'lab/solve.html', context)

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
    # check if the user is authenticated
    # if not redirect to login page
    # if the authenticated user is a student
    # redirect to assignments page for students
    submission = AssignmentSubmissions.objects.get(id=pk)
    if submission:
        if request.method == 'POST':
            # if 'run_code' in request.post
            # define the assignment submissions path
            # run the code
            # add the code results to the context
            # display the code results to the teacher
            if 'runcode' in request.POST:
                code_name = submission.code.name
                try:
                    compile_code = os.popen('gcc -lm ' + assignment_submission_path + code_name)
                    execute_code = os.popen('./a.out < ' + assignment_submission_path+'sol.txt')
                    print(execute_code)
                    return HttpResponse(execute_code)
                except Exception as e:
                    return HttpResponse(e)

            if 'accepted' in request.POST:
                remarks = request.POST.get('remarks')
                # take the remarks
                # update the submission model to mark it as accepted
                # update teachers_remarks if given any
                submission.approved = True
                submission.teachers_remarks = remarks
                submission.reviewed = True
                submission.save()
                return HttpResponse('Accepted')
            elif 'rejected' in request.POST:
                remarks = request.POST.get('remarks')
                # same but do not mark this submission as accepted
                submission.teachers_remarks = remarks
                submission.reviewed = True
                submission.save()
                return HttpResponse('Rejected!')
        else:
            # query the submission
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
            # query rejected assignments
            rejected_submissions = AssignmentSubmissions.objects.filter(reviewed=True, approved=False)
            accepted_submissions = AssignmentSubmissions.objects.filter(reviewed=True, approved=True)
            if assignments:
                context = {
                    'problems': assignments,
                    'rejected_submissions': rejected_submissions,
                    'accepted_submissions': accepted_submissions
            }
            else:
                context = {
                    'alert': "No assignments given yet."
                }
            for sub in accepted_submissions:
                print(sub.problem.title)
            for s in rejected_submissions:
                print(s.teachers_remarks)
            return render(request, 'lab/labexp.html', context)
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
                return render(request, 'lab/solve.html', context)
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











# CHECKING REJECTED SUBMISSIONS
# for students
def rejectedSubmissions(request, pk):
    # check if the user is authenticated
    # redirect to login if not
    # otherwise check if it is a student
    # redirect to labs if not
    if request.user.is_authenticated:
        # check if the user is a student
        if request.user.position == 'Student':
            rejected_submission = AssignmentSubmissions.objects.get(id = pk)
            code = rejected_submission.code
            code = code.read().decode('utf-8')
            context = {
                'rejected_submission':rejected_submission,
                'code':code
            }
            return render(request, 'lab/rejects.html', context)
        else:
            # redirect to labs
            return redirect('lab-labproblems')
    else:
        return redirect('user-login')

## Accepted Assignments
## for students
def acceptedSubmissions(request, pk):
    # check if the user is authenticated
    # redirect to login if not
    # otherwise check if it is a student
    # redirect to labs if not
    if request.user.is_authenticated:
        # check if the user is a student
        if request.user.position == 'Student':
            accepted_submission = AssignmentSubmissions.objects.get(id = pk)
            code = accepted_submission.code
            code = code.read().decode('utf-8')
            context = {
                'accepted_submission':accepted_submission,
                'code':code
            }
            return render(request, 'lab/accepted.html', context)
        else:
            # redirect to labs
            return redirect('lab-labproblems')
    else:
        return redirect('user-login')

