from os import path as os_path
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Journal, Distortion
from .forms import JournalForm,EmotionFormSet,ThoughtFormSet

@login_required
def index(request):
    journal_list = Journal.objects.order_by('-create_date')
    error=int(request.GET.get('error',0))
    context = {'page_title': "Home", 'journal_list': journal_list, "error": error}
    return render(request, 'index.html', context)

@login_required
def cru(request,journal_id=None):
    if journal_id:
        j = Journal.objects.get(pk=journal_id)
    else:
        j = Journal()
    if request.method == "POST":
        jf = JournalForm(request.POST, request.FILES, instance=j)
        efs = EmotionFormSet(request.POST, request.FILES, instance=j)
        tfs = ThoughtFormSet(request.POST, request.FILES, instance=j)
        if jf.is_valid() and efs.is_valid() and tfs.is_valid():
            jf.save()
            efs.save()
            tfs.save()
            return HttpResponseRedirect("/")
        else:
            print("Journal form errors: "+str(jf.errors))
            print("Emotion formset errors: "+str(efs.errors))
            print("Thought formset errors: "+str(tfs.errors))
            return HttpResponseRedirect("/?error=1")
    else:
        jf = JournalForm(instance=j)
        efs = EmotionFormSet(instance=j)
        tfs = ThoughtFormSet(instance=j)
        url_path = os_path.basename(request.path.strip("/")).capitalize()
        if url_path == "Read":
            for field in jf:
                field.field.disabled=True
            for form in efs:
                for field in form:
                    field.field.disabled=True
            for form in tfs:
                for field in form:
                    field.field.disabled=True
        distortions_dict={}
        for distortion in Distortion.objects.all():
            distortions_dict[distortion.name]=distortion.description.replace("'","\\u0027")
        context = {
            'page_title': url_path,
            'journal_id': journal_id,
            'jf': jf,
            'efs': efs,
            'tfs': tfs,
            'distortions_dict_str': json.dumps(distortions_dict)
            }
        return render(request, 'cru.html', context)
