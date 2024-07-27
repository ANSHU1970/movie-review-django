from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello peeps!! you are at beginDjango homepage.")
    return render(request,'index.html')