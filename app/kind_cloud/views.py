from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Kind
from .forms import KindForm

def index(request):
    kinds = Kind.objects.all().order_by('-votes')
    return render(request, 'view_all.html', {
        'kinds': kinds,
    })

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

def upvote(_, kind_id):
    kind = Kind.objects.get(id=kind_id)
    kind.votes += 1
    kind.save()
    return HttpResponseRedirect('/')

@user_passes_test(lambda u: u.is_superuser, '/admin')
def admin(request):
    kinds = Kind.objects.all()
    return render(request, 'admin_edit.html', {
        'kinds': kinds,
    })

@user_passes_test(lambda u: u.is_superuser, '/admin')
def delete(request):
    if request.method == 'POST':
        kind_id = request.POST.get('kind_id')
        kind = Kind.objects.get(id=kind_id)
        kind.delete()
    return HttpResponseRedirect('/admin-edit')
