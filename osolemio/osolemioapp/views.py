from django.shortcuts import render

# Create your views here.

def mivista(request):
    return render(request, 'osolemioapp/index.html')