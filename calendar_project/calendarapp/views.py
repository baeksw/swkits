from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import UserSerializer, GroupSerializer, EntrySerializer

from django.contrib.auth.models import User, Group

from .models import Entry
from .forms import EntryForm

# https://github.com/pivotal-energy-solutions/django-datatable-view/blob/master/datatableview/tests/example_project/example_project/example_app/views.py
# https://datatables.net/forums/discussion/45215/django-rest-framework-and-datatableS


def index(request):
    return render(request,'intro/intro.html')

def calendar(request):
    entries = Entry.objects.all()
    return render(request,'calendarapp/calendar.html', {'entries' : entries })
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class EntryPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.all()

def details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request,'calendarapp/detail.html', {'entry' : entry })


def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            Entry.objects.create(name=name, date=date, description=description).save()
            #return HttpResponseRedirect('/')
            return redirect('calendar')

    else:
        form = EntryForm()

    return render(request, 'calendarapp/form.html', {'form' : form})



def delete(request, pk):

    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')
