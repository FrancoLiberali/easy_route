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
                "info": "Cheapest",
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
                            "duration": "1h20m"
                        }
                    },
                    {
                        "city_name": "Dublin",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Dublin Airport",
                            "destination": "Edinburgh Airport",
                            "origin_acronym": "DUB",
                            "destination_acronym": "EDI",
                            "day": (start_date + timedelta(days=3)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Edinburgh",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Edinburgh Airport",
                            "destination": "London Airport",
                            "origin_acronym": "DUB",
                            "destination_acronym": "LON",
                            "day": (start_date + timedelta(days=6)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "London",
                        "duration": 6,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "London Airport",
                            "destination": "Berlin Airport",
                            "origin_acronym": "LON",
                            "destination_acronym": "BER",
                            "day": (start_date + timedelta(days=12)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Berlin",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Berlin Airport",
                            "destination": "Prague Airport",
                            "origin_acronym": "BER",
                            "destination_acronym": "PRA",
                            "day": (start_date + timedelta(days=15)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Prague",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Prague Airport",
                            "destination": "Bratislava Airport",
                            "origin_acronym": "PRA",
                            "destination_acronym": "BRA",
                            "day": (start_date + timedelta(days=18)).strftime(DATE_FORMAT),
                            "duration": "1h25m"
                        }
                    },
                    {
                        "city_name": "Bratislava",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Bratislava Airport",
                            "destination": "Budapest Airport",
                            "origin_acronym": "BRA",
                            "destination_acronym": "BUD",
                            "day": (start_date + timedelta(days=20)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Budapest",
                        "duration": 5,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Budapest Airport",
                            "destination": "Athens Airport",
                            "origin_acronym": "BUD",
                            "destination_acronym": "ATH",
                            "day": (start_date + timedelta(days=25)).strftime(DATE_FORMAT),
                            "duration": "1h30m"
                        }
                    },
                    {
                        "city_name": "Athens",
                        "duration": 5,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Athens Airport",
                            "destination": "Nantes Airport",
                            "origin_acronym": "ATH",
                            "destination_acronym": "NAN",
                            "day": (start_date + timedelta(days=30)).strftime(DATE_FORMAT),
                            "duration": "1h40m"
                        }
                    },
                    {"city_name": "Nantes"},
                ]
            }
        )
        routes.append(
            {
                "price": "€600",
                "info": "Recommended",
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
                            "duration": "1h20m"
                        }
                    },
                    {
                        "city_name": "Dublin",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Dublin Airport",
                            "destination": "Edinburgh Airport",
                            "origin_acronym": "DUB",
                            "destination_acronym": "EDI",
                            "day": (start_date + timedelta(days=2)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "Edinburgh",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Dublin Airport",
                            "destination": "Edinburgh Airport",
                            "origin_acronym": "DUB",
                            "destination_acronym": "LON",
                            "day": (start_date + timedelta(days=4)).strftime(DATE_FORMAT),
                            "duration": "1h5m"
                        }
                    },
                    {
                        "city_name": "London",
                        "duration": 4,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "London Airport",
                            "destination": "Amsterdam Airport",
                            "origin_acronym": "LON",
                            "destination_acronym": "AMS",
                            "day": (start_date + timedelta(days=8)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Amsterdam",
                        "duration": 4,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Amsterdam Airport",
                            "destination": "Budapest Airport",
                            "origin_acronym": "AMS",
                            "destination_acronym": "BUD",
                            "day": (start_date + timedelta(days=12)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Budapest",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Budapest Airport",
                            "destination": "Rome Airport",
                            "origin_acronym": "BUD",
                            "destination_acronym": "ROM",
                            "day": (start_date + timedelta(days=15)).strftime(DATE_FORMAT),
                            "duration": "1h25m"
                        }
                    },
                    {
                        "city_name": "Rome",
                        "duration": 4,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Rome Airport",
                            "destination": "Venice Airport",
                            "origin_acronym": "ROM",
                            "destination_acronym": "VEN",
                            "day": (start_date + timedelta(days=19)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Venice",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Venice Airport",
                            "destination": "Barcelona Airport",
                            "origin_acronym": "VEN",
                            "destination_acronym": "BAR",
                            "day": (start_date + timedelta(days=21)).strftime(DATE_FORMAT),
                            "duration": "1h25m"
                        }
                    },
                    {
                        "city_name": "Barcelona",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Barcelona Airport",
                            "destination": "Madrid Airport",
                            "origin_acronym": "BAR",
                            "destination_acronym": "MAD",
                            "day": (start_date + timedelta(days=24)).strftime(DATE_FORMAT),
                            "duration": "1h20m"
                        }
                    },
                    {
                        "city_name": "Madrid",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Madrid Airport",
                            "destination": "Lisbon Airport",
                            "origin_acronym": "MAD",
                            "destination_acronym": "LIS",
                            "day": (start_date + timedelta(days=27)).strftime(DATE_FORMAT),
                            "duration": "1h40m"
                        }
                    },
                    {
                        "city_name": "Lisbon",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Lisbon Airport",
                            "destination": "Nantes Airport",
                            "origin_acronym": "LIS",
                            "destination_acronym": "NAN",
                            "day": (start_date + timedelta(days=30)).strftime(DATE_FORMAT),
                            "duration": "1h40m"
                        }
                    },
                    {"city_name": "Nantes"},
                ]
            }
        )
        routes.append(
            {
                "price": "€1000",
                "info": "Classic",
                "places": [
                    {
                        "city_name": "Nantes",
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Nantes Airport",
                            "destination": "London Airport",
                            "origin_acronym": "NAN",
                            "destination_acronym": "LON",
                            "day": start_date_string,
                            "duration": "1h20m"
                        }
                    },
                    {
                        "city_name": "London",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "London Airport",
                            "destination": "Paris Airport",
                            "origin_acronym": "LON",
                            "destination_acronym": "PAR",
                            "day": (start_date + timedelta(days=3)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Paris",
                        "duration": 5,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Paris Airport",
                            "destination": "Amsterdam Airport",
                            "origin_acronym": "PAR",
                            "destination_acronym": "AMS",
                            "day": (start_date + timedelta(days=8)).strftime(DATE_FORMAT),
                            "duration": "1h15m"
                        }
                    },
                    {
                        "city_name": "Amsterdam",
                        "duration": 3,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Amsterdam Airport",
                            "destination": "Berlin Airport",
                            "origin_acronym": "AMS",
                            "destination_acronym": "BER",
                            "day": (start_date + timedelta(days=11)).strftime(DATE_FORMAT),
                            "duration": "1h25m"
                        }
                    },
                    {
                        "city_name": "Berlin",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Berlin Airport",
                            "destination": "Prague Airport",
                            "origin_acronym": "BER",
                            "destination_acronym": "PRA",
                            "day": (start_date + timedelta(days=13)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Prague",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Prague Airport",
                            "destination": "Venice Airport",
                            "origin_acronym": "PRA",
                            "destination_acronym": "VEN",
                            "day": (start_date + timedelta(days=15)).strftime(DATE_FORMAT),
                            "duration": "1h25m"
                        }
                    },
                    {
                        "city_name": "Venice",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Venice Airport",
                            "destination": "Rome Airport",
                            "origin_acronym": "VEN",
                            "destination_acronym": "ROM",
                            "day": (start_date + timedelta(days=17)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
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
                            "day": (start_date + timedelta(days=22)).strftime(DATE_FORMAT),
                            "duration": "1h10m"
                        }
                    },
                    {
                        "city_name": "Milan",
                        "duration": 2,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Milan Airport",
                            "destination": "Barcelona Airport",
                            "origin_acronym": "MIL",
                            "destination_acronym": "BAR",
                            "day": (start_date + timedelta(days=24)).strftime(DATE_FORMAT),
                            "duration": "1h30m"
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
                            "day": (start_date + timedelta(days=26)).strftime(DATE_FORMAT),
                            "duration": "1h20m"
                        }
                    },
                    {
                        "city_name": "Madrid",
                        "duration": 4,
                        "next_travel": {
                            "transport_type": AIRPLANE,
                            "origin": "Madrid Airport",
                            "destination": "Nantes Airport",
                            "origin_acronym": "MAD",
                            "destination_acronym": "NAN",
                            "day": (start_date + timedelta(days=30)).strftime(DATE_FORMAT),
                            "duration": "1h40m"
                        }
                    },
                    {"city_name": "Nantes"},
                ]
            }
        )
    context["routes"] = routes
    context["result_amount"] = 12
    return render(request, 'search.html', context)
