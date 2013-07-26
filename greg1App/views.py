# Create your views here.

from django.shortcuts import render_to_response
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from greg1App.models import Person

def home(request):
	return render_to_response('greg1App/home.html')

class PersonCreateView(CreateView):
	model = Person

class PersonUpdateView(UpdateView):
	model = Person
