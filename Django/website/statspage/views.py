from django.shortcuts import render
from django.http import HttpResponse, Http404
import pandas as pd

def stats(request):
    return render(request, "statspage/index.html")