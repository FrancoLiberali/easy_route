from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'index.html', request.POST.dict())
