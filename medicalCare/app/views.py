from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import  JsonResponse

#  your views here.
def index(request):
    
    return render(request, 'index.html')
@csrf_exempt
def add_eias(request):
    data = dict(request.POST)
    eias = {}
    for element in data :
        eias[element] = data[element][0]
    f = open("app/eias.json", "rb")
    list_eias = json.load(f)
    f.close()
    list_eias[len(list(list_eias.keys()))] = eias
    print(list_eias)
    f = open("app/eias.json", "w")
    json.dump(list_eias,f)
    f.close()
    return redirect("/")

@login_required
def admin(request):
    f = open("app/eias.json", "r")
    EIAS = json.load(f)
    return render(request, 'admin.html', {"EIAS":EIAS})

@csrf_exempt
def get_data(request, id=None):
    f = open("app/eias.json", "rb")
    list_eias = json.load(f)
    f.close()
    data = list_eias.get(id)
    if data :
        print(len(data))
        return JsonResponse(data)
    else :
        return JsonResponse({})