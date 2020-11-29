from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Journal

@login_required
def index(request):
    journal_list = Journal.objects.order_by('-create_date')
    context = {'page_title': "Home", 'journal_list': journal_list}
    return render(request, 'index.html', context)

@login_required
def create(request):
    context = {'page_title': "Create"}
    return render(request, 'crud.html', context)

@login_required
def edit(request,journal_id):
    context = {'page_title': "Edit", 'journal_id': journal_id}
    return render(request, 'crud.html', context)

@login_required
def read(request,journal_id):
    context = {'page_title': "Read", 'journal_id': journal_id}
    return render(request, 'crud.html', context)