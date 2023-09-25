from django.shortcuts import render
from django.http import HttpResponse, Http404
import pandas as pd

def signup(request):
    return render(request, "signuppage/index.html")



