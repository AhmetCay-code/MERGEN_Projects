from django.shortcuts import render
from django.http import HttpResponse, Http404
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

# adding full path of csv doc!!
country_names=['germany','england','france','italy','spain']
for i in country_names:
    file = open('C:/Users/ahmet/Desktop/MERGEN/Django/website/static/prediction_'+str(i)+'.csv')
    df=pd.read_csv(file)
    len_of_pd=len(df)
    globals()[f'{i}_db'] = df.assign(ColumnA = df.HomeTeam.astype(str) + ' - ' + df.AwayTeam.astype(str) + ' :  ' + df.label.astype(str) + ' WITH %' + df.probablity.astype(str) + ' PROBABLITY')

texts_ger = []
for i in range(len(germany_db)):
    texts_ger.append(germany_db.ColumnA[i])

texts_eng = []
for i in range(len(england_db)):
    texts_eng.append(england_db.ColumnA[i])

texts_fra = []
for i in range(len(france_db)):
    texts_fra.append(france_db.ColumnA[i])

texts_ita = []
for i in range(len(italy_db)):
    texts_ita.append(italy_db.ColumnA[i])

texts_spa = []
for i in range(len(spain_db)):
    texts_spa.append(spain_db.ColumnA[i])


def section1(request, num):
    if 1 <= num <= 10:
        return HttpResponse(texts_eng[num-1])
    else:
        raise Http404("No such section")
    
def section2(request, num):
    if 1 <= num <= 10:
        return HttpResponse(texts_fra[num-1])
    else:
        raise Http404("No such section")
    
def section3(request, num):
    if 1 <= num <= 10:
        return HttpResponse(texts_ita[num-1])
    else:
        raise Http404("No such section")
    
def section4(request, num):
    if 1 <= num <= 10:
        return HttpResponse(texts_ger[num-1])
    else:
        raise Http404("No such section")
    
def section5(request, num):
    if 1 <= num <= 10:
        return HttpResponse(texts_spa[num-1])
    else:
        raise Http404("No such section")