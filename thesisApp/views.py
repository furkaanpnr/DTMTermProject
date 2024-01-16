from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ThesisCreationForm
from .helpers import _paginator
from .models import University, Institute, SubjectTopic, Thesis
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    featured_thesis_list = Thesis.objects.all().order_by('-submission_date')[:3]

    context = {
        'featured_theses': featured_thesis_list
    }

    return render(request, 'thesis/home.html', context)

def thesis(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
    
    # filter the thesis by query for:
    if query:
        thesis_list = Thesis.objects.filter(title__icontains=query, abstract__icontains=query)
    else:
        thesis_list = Thesis.objects.all()
    
    # pagination
    thesis_list = _paginator(request, thesis_list, num_per_page=15)

    context = {'thesis_list': thesis_list}
    return render(request, 'thesis/thesis.html', context)

def thesis_detail(request, thesis_id):
    thesis = Thesis.objects.get(id=thesis_id)
    context = {'thesis': thesis}
    return render(request, 'thesis/thesis_detail.html', context)

def new_thesis_request(request):

    admin_furkan = User.objects.get(username='furkanpnr')

    if request.method == 'POST':
        form = ThesisCreationForm(request.POST)
        if form.is_valid():
            thesis = form.save(commit=False)
            thesis.author = request.user
            thesis.supervisor = admin_furkan
            thesis.save()
            return redirect('profile')
        else:
            # redirect to the profile page with error messages
            return render(request, 'account/profile.html', {
                'form': form,
                'messages': form.errors.values()
            })
