from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from archemywebapp.forms import *
from django.forms import *
import os
from subprocess import Popen,STDOUT,PIPE

# Create your views here.
@login_required
def index(request):
	return render(request, 'archemywebapp/index.html', {})

@csrf_exempt
def login(request):
    next = request.GET.get('next', '/index/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "archemywebapp/login_view.html", {'redirect_to': next})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

@csrf_exempt
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            args = ['java','-jar','./archemy-security-1.0-SNAPSHOT-jar-with-dependencies.jar','-cuser','-u',form.cleaned_data['username'],'-p',form.cleaned_data['password1'],'-r','NormalUser','-utype','normal']
            process = Popen(args, stdout=PIPE, stderr=STDOUT)
            for line in process.stdout:
                print line
            return HttpResponseRedirect('/register/success/')
    form = RegistrationForm()
    '''variables = RequestContext(request, {'form': form})'''
    return render_to_response('archemywebapp/register_view.html', {'form': form}, RequestContext(request))

def register_success(request):
    return render(request, 'archemywebapp/register_success.html')

@login_required
def ExploreCatalogue(request):
	return render(request, 'archemywebapp/ExploreCatalogue.html')

def ArchDev(request):
	return render(request, 'archemywebapp/ArchDev.html', {})

def AdaptiveReuse(request):
	return render(request, 'archemywebapp/AdaptiveReuse.html', {})

def AEL(request):
	return render(request, 'archemywebapp/Ael.html', {})

def AelIdeation(request):
	return render(request, 'archemywebapp/AelIdeation.html', {})

def AelInception(request):
	return render(request, 'archemywebapp/AelInception.html', {})

def AelElaboration(request):
	return render(request, 'archemywebapp/AelElaboration.html', {})

def AelImplementation(request):
	return render(request, 'archemywebapp/AelImplementation.html', {})

def AelDeployment(request):
	return render(request, 'archemywebapp/AelDeployment.html', {})

def AelOperations(request):
	return render(request, 'archemywebapp/AelOperations.html', {})

def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret