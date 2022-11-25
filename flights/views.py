from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def search(request):
    print(request.POST.dict())
    return render(request, 'search.html', request.POST.dict())
