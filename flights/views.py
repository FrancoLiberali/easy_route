from django.shortcuts import render
from datetime import date, timedelta

def index(request):
    context = {}
    context["destination"] = "Europe"
    today = date.today()
    context["from"] = today.strftime("%Y-%m-%d")
    context["to"] = (today + timedelta(weeks=8)).strftime("%Y-%m-%d")
    context["duration"] = 30
    context["passenger"] = 1
    return render(request, 'index.html', context)

def search(request):
    context = request.POST.dict()
    context["result_amount"] = 12
    return render(request, 'search.html', context)
