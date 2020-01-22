import requests
from requests.exceptions import HTTPError

get_routes = "http://svc.metrotransit.org/NexTrip/Routes"
Get_stops = "http://svc.metrotransit.org/NexTrip/Stops/{}/{}"
Get_timepoint = "http://svc.metrotransit.org/NexTrip/{}/{}/{}"

def request_route():
    try:
        response = requests.get(get_routes, headers={'Content-Type':'application/json', 'Accept': 'application/json'})
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')

    else:
        return response.json()
    pass