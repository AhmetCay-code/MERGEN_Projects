from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
def login(request):
    form = UserCreationForm()
    context= {'form':form}
    return render(request, "loginpage/index.html")