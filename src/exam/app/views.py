from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from app.models import Exam

def index(request):
    if request.user.is_authenticated():
        exam_list = Exam.objects.all()
        return render(request, 'app/index.html', {'exam_list': exam_list})
    else:
        return render(request, 'app/login.html', {'not_in':True})
        #return redirect('app:login')        

def view(request, exam_id):
    if request.user.is_authenticated():
        exam = get_object_or_404(Exam, pk=exam_id)
        return render(request, 'app/view.html', {'exam': exam})
    else:
        return render(request, 'app/login.html', {'not_in':True})

def result(request, exam_id):
    if request.user.is_authenticated():
        exam = get_object_or_404(Exam, pk=exam_id)
        return render(request, 'app/result.html', {'exam': exam})
    else:
        return render(request, 'app/login.html', {'not_in':True})

def login_view(request):
    if request.user.is_authenticated():
        return redirect('app:index')
    if request.method == 'GET':
        return render(request, 'app/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
	    if user.is_active:
	        login(request, user)
                return HttpResponseRedirect(reverse('app:index'))
	        #return redirect('app:index')
	    else:
	        return HttpResponse('Disabled Account')
        else:
	    return render(request, 'app/login.html', {'invalid':True})

def logout_view(request):
    logout(request)
    return redirect('app:login')

def calc(request, exam_id):
    #take in varaibles answers and number of questions
    #calculate total score
    #inc exam.times_taken
    return redirect('app:index')
