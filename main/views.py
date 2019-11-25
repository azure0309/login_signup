from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.
def index(response, id):
	ls = ToDoList.objects.get(id=id)
	return render(response, 'main/list.html', {'ls': ls})


def home(response):
	return render(response, 'main/home.html', {})


def create(response):
	if response.method == "GET":
		form = CreateNewList()

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			return HttpResponseRedirect(f'{t.id}')
	else:
		form = CreateNewList()
	return render(response, 'main/create.html', {"form": form})
