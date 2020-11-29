from os import path as os_path

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
def cru(request,journal_id=None):
    if journal_id:
        j = Journal.objects.get(pk=journal_id)
    else:
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
            #TODO
            pass
    else:
        jf = JournalForm(instance=j)
        efs = EmotionFormSet(instance=j)
        tfs = ThoughtFormSet(instance=j)
        context = {
            'page_title': os_path.basename(request.path.strip("/")).capitalize(),
            'journal_id': journal_id,
            'jf': jf,
            'efs': efs,
            'tfs': tfs
            }
        return render(request, 'cru.html', context)
