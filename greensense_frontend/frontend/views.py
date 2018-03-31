from django.shortcuts import render
from django.http import HttpResponse
from frontend.temppredict import temperature
from frontend.firebase import firebase_img
import requests
import json
import pyrebase
from frontend.temp import firebase_get
from frontend.weatherforecast import forecast5

from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):


    if 'upload' in request.POST:
        return render(request,'simple_upload.html')

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
    m=firebase_get()
    return render(request, 'index.html' ,{'output': fah1,'read':m})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = (filename)
        py_obj=uploaded_file_url
        firebase_img(py_obj)
        return render(request, 'output.html' ,{'output': py_obj})

    return render(request, 'simple_upload.html')
