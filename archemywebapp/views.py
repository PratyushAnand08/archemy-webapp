from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.forms import *

# Create your views here.

def index(request):
	return render(request, 'archemywebapp/index.html', {})

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