from django.shortcuts import render
from datetime import date, timedelta, datetime

DATE_FORMAT = "%Y-%m-%d"
AIRPLANE = "AIRPLANE"
BUS = "BUS"
TRAIN = "TRAIN"

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
                "info": "Most popular",
                "places": [
                    {
                        "city_name": "Nantes",
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Nantes Airport",
                            "destination": "Dublin Airport",
                            "origin_acronym": "NAN",
                            "destination_acronym": "DUB",
                            "day": start_date_string,
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Dublin",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Dublin Airport",
                            "destination": "London Airport",
                            "origin_acronym": "DUB",
                            "destination_acronym": "LON",
                            "day": (start_date + timedelta(days=2)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "London",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "London Airport",
                            "destination": "Amsterdam Airport",
                            "origin_acronym": "LON",
                            "destination_acronym": "AMS",
                            "day": (start_date + timedelta(days=5)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Amsterdam",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Amsterdam Airport",
                            "destination": "Berlin Airport",
                            "origin_acronym": "AMS",
                            "destination_acronym": "BER",
                            "day": (start_date + timedelta(days=7)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Berlin",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Berlin Airport",
                            "destination": "Rome Airport",
                            "origin_acronym": "BER",
                            "destination_acronym": "ROM",
                            "day": (start_date + timedelta(days=9)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Rome",
                        "duration": 5,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Rome Airport",
                            "destination": "Milan Airport",
                            "origin_acronym": "ROM",
                            "destination_acronym": "MIL",
                            "day": (start_date + timedelta(days=11)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Milan",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Milan Airport",
                            "destination": "Paris Airport",
                            "origin_acronym": "MIL",
                            "destination_acronym": "PAR",
                            "day": (start_date + timedelta(days=16)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Paris",
                        "duration": 5,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Paris Airport",
                            "destination": "Barcelona Airport",
                            "origin_acronym": "PAR",
                            "destination_acronym": "BAR",
                            "day": (start_date + timedelta(days=13)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Barcelona",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Barcelona Airport",
                            "destination": "Madrid Airport",
                            "origin_acronym": "BAR",
                            "destination_acronym": "MAD",
                            "day": (start_date + timedelta(days=18)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Madrid",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Madrid Airport",
                            "destination": "Nantes Airport",
                            "origin_acronym": "MAD",
                            "destination_acronym": "NAN",
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
