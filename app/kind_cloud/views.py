from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Kind
from .forms import KindForm

def index(request):
    kinds = Kind.objects.all()
    return render(request, 'view_all.html', {'kinds': kinds})

def create(request):
    if request.method == 'POST':
        form = KindForm(request.POST)
        if form.is_valid():
            kind = form.save()
            kind.save()
            return HttpResponseRedirect('/')
    else:
        form = KindForm()
    return render(request, 'create.html', {'form': form})
