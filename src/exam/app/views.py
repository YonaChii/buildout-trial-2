from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from app.models import Exam

def index(request):
    exam_list = Exam.objects.all()[:5]
    return render(request, 'app/index.html', {'exam_list': exam_list})

def view(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'app/view.html', {'exam': exam})

def result(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'app/result.html', {'exam': exam})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
	if user.is_active:
	    login(request, user)
	# Redirect to a success page.
	else:
	    pass
	# Return a disabled account error message
    else:
	pass
	# Return an invalid login error message.

def logout(request):
    logout(request)

def calc(request, exam_id):
    #calculate score
    #store score get average
    #inc exam.times_taken
    return HttpResponse("calculating exam score")