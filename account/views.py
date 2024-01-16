from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .helpers import _paginator
from thesisApp.models import Thesis
from thesisApp.forms import ThesisCreationForm
from copy import deepcopy

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, "Form is not valid!")
            return HttpResponseRedirect('/account/login')

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is None:
            messages.error(request, "Username or password is wrong!")
            return HttpResponseRedirect('/account/login')
        
        login(request, user)
        messages.success(request, "Login successful.")
        return redirect('home')

    return render(request, 'account/login.html', {
        'form': LoginForm()
    })

def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if not form.is_valid():
            messages.error(request, "Form is not valid!")
            return HttpResponseRedirect('/account/register')

        if form.cleaned_data['password'] != form.cleaned_data['password2']:
            messages.error(request, "Passwords do not match!")
            return HttpResponseRedirect('/account/register')
        
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            messages.error(request, "User already exists!")
            return HttpResponseRedirect('/account/register')
        
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        user.save()
        messages.success(request, "Register successful.")
        return redirect('home')
    

    return render(request, 'account/register.html', {
        'form': RegisterForm()
    })

def logout_request(request):
    logout(request)
    return redirect('home')

def profile(request):
    user_thesis = Thesis.objects.filter(author__id=request.user.id)
    
    new_thesis_form =  ThesisCreationForm()

    # # Test pagination
    # # query set has 1 thesis object we need to clone it for 20 times to test pagination
    # thesis_list = []
    # for i in range(20):
    #     thesis_list.append(deepcopy(user_thesis[0]))
    
    # for thesis in thesis_list[10:]:
    #     thesis.title = f"{thesis.title}--{i}"

    # pagination
    thesis_list = _paginator(request, user_thesis, 10)

    context = {
        'thesis_list': thesis_list,
        'form': new_thesis_form,
    }
    return render(request, 'account/profile.html', context)