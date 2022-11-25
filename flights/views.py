from django.shortcuts import render
from datetime import date, timedelta, datetime

DATE_FORMAT = "%Y-%m-%d"

def index(request):
    context = {}
    context["destination"] = "Europe"
    today = date.today()
    context["from"] = today.strftime(DATE_FORMAT)
    context["to"] = (today + timedelta(weeks=8)).strftime(DATE_FORMAT)
    context["duration"] = 30
    context["passenger"] = 1
    return render(request, 'index.html', context)

def search(request):
    context = request.POST.dict()

    start_date_string = context["from"]
    start_date = datetime.strptime(start_date_string, DATE_FORMAT)

    routes = []
    if context["destination"] == "Europe":
        routes.append(
            {
                "price": "€400",
                "places": [
                    {
                        "city_name": "Nantes",
                        "next_travel": {
                            "day": start_date_string,
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Dublin",
                        "duration": 2,
                        "next_travel": {
                            "day": (start_date + timedelta(days=2)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "London",
                        "duration": 3,
                        "next_travel": {
                            "day": (start_date + timedelta(days=5)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Amsterdam",
                        "duration": 2,
                        "next_travel": {
                            "day": (start_date + timedelta(days=7)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Berlin",
                        "duration": 2,
                        "next_travel": {
                            "day": (start_date + timedelta(days=9)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Rome",
                        "duration": 5,
                        "next_travel": {
                            "day": (start_date + timedelta(days=11)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Milan",
                        "duration": 2,
                        "next_travel": {
                            "day": (start_date + timedelta(days=16)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Paris",
                        "duration": 5,
                        "next_travel": {
                            "day": (start_date + timedelta(days=13)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Barcelona",
                        "duration": 2,
                        "next_travel": {
                            "day": (start_date + timedelta(days=18)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Madrid",
                        "duration": 3,
                        "next_travel": {
                            "day": (start_date + timedelta(days=20)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {"city_name": "Nantes"},
                ]
            }
        )
    context["routes"] = routes
    context["result_amount"] = 12
    return render(request, 'search.html', context)
