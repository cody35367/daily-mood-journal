from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Journal
from .forms import JournalForm,EmotionFormSet,ThoughtFormSet

@login_required
def index(request):
    journal_list = Journal.objects.order_by('-create_date')
    context = {'page_title': "Home", 'journal_list': journal_list}
    return render(request, 'index.html', context)

@login_required
def create(request):
    j = Journal()
    if request.method == "POST":
        jf = JournalForm(request.POST, request.FILES,instance=j)
        efs = EmotionFormSet(request.POST, request.FILES, instance=j)
        tfs = ThoughtFormSet(request.POST, request.FILES, instance=j)
        if jf.is_valid() and efs.is_valid() and tfs.is_valid():
            jf.save()
            efs.save()
            tfs.save()
            return HttpResponseRedirect("/")
    else:
        jf = JournalForm(instance=j)
        efs = EmotionFormSet(instance=j)
        tfs = ThoughtFormSet(instance=j)
        context = {
            'page_title': "Create",
            'jf': jf,
            'efs': efs,
            'tfs': tfs
            }
        return render(request, 'crud.html', context)

@login_required
def edit(request,journal_id):
    context = {'page_title': "Edit", 'journal_id': journal_id}
    return render(request, 'crud.html', context)

@login_required
def read(request,journal_id):
    context = {'page_title': "Read", 'journal_id': journal_id}
    return render(request, 'crud.html', context)