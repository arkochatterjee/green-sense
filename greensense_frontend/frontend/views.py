from django.shortcuts import render
from django.http import HttpResponse
from frontend.temppredict import temperature
from frontend.firebase0 import firebase_img
import requests
import json
import pyrebase
from frontend.temp import firebase_get
from frontend.weatherforecast import forecast5

from django.core.files.storage import FileSystemStorage


smos=""
amos=""
atemp=""
ph=0
# Create your views here.
def index(request):




    if 'WebsiteS' in request.POST:
        screenname2 = request.POST.get("Website", None)
        predict2 = screenname2
        print(predict2)
        #api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = predict2

        #url = api_address + city
        #city1='Chennai'
        #url1 = api_address + city1
        #json_data = requests.get(url).json()
        #json_data1 = requests.get(url1).json()
        #fah=json_data['main']['temp_max']
        #fah1=json_data1['main']['temp_max']
        #print(json_data)
        return render(request, 'output.html' ,{'output': forecast5(city)})
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city1='Chennai'
    url1 = api_address + city1
    json_data1 = requests.get(url1).json()
    fah1=json_data1['main']['temp_max']
    data=firebase_get()
    a = data["Data1"]
    print(a)

    b = a[0]
    print(b)
    if b == "1":
	    ph = "HIGH"
    else:
        ph = "LOW"
    print(ph)
    #print(type(a))

    for i in range(0,len(a)):
	       if a[i] == ",":
  	            smos = a[(i+1):(i+5)]
                #print(smos)
    for j in range(0,len(a)):
	       if a[j] == "!":
  	            amos = a[(j+1):(j+6)]
                #print(amos)
    for k in range(0,len(a)):
	       if a[k] == "@":
  	            atemp = a[(k+1):(k+6)]
                #print(atemp)
    for l in range (0,len(a)):
	       if a[l] == ";":
  	            min = a[(l+1):len(a)]
                #minsun = (int(min)*12)/60

    return render(request, 'index.html' ,{'live':forecast5("Vellore"),'output': fah1,'ph': ph,'smos': smos,'amos': amos,'atemp': atemp,'min': min})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = (filename)
        py_obj=uploaded_file_url
        print(py_obj)
        firebase_img(py_obj)
        return render(request, 'simple_upload.html' ,{'message': "Image Successfully Uploaded!"})

    return render(request, 'simple_upload.html')

def plant_more(request):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city1='Chennai'
    url1 = api_address + city1
    json_data1 = requests.get(url1).json()
    fah1=json_data1['main']['temp_max']
    #t=int(float(atemp))

    data=firebase_get()
    a = data["Data1"]
    print(a)

    b = a[0]
    print(b)
    if b == "1":
	    ph = "HIGH"
    else:
        ph = "LOW"
    print(ph)
    #print(type(a))

    for i in range(0,len(a)):
	       if a[i] == ",":
  	            smos = a[(i+1):(i+5)]
                #print(smos)
    for j in range(0,len(a)):
	       if a[j] == "!":
  	            amos = a[(j+1):(j+6)]
                #print(amos)
    for k in range(0,len(a)):
	       if a[k] == "@":
  	            atemp = a[(k+1):(k+6)]
                #print(atemp)
    for l in range (0,len(a)):
	       if a[l] == ";":
  	            min = a[(l+1):len(a)]
                #minsun = (int(min)*12)/60

    atemp=(float(atemp))
    print(type(atemp))
    T=str(int((atemp+(fah1-273))/2))+" °C"
    A=str(amos)+"%"
    S=str(smos)+"%"
    f=T+" | "+A+" | "+S
    if(T>="0"):
        return render(request,'plant_new.html',{'output':f,'message': "Irrigation Required!"})
    return render(request,'plant_new.html',{'output':f})
