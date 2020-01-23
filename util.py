import requests
from requests.exceptions import HTTPError

get_routes = "http://svc.metrotransit.org/NexTrip/Routes"
get_stops = "http://svc.metrotransit.org/NexTrip/Stops/{}/{}"
get_timepoint = "http://svc.metrotransit.org/NexTrip/{}/{}/{}"

def base_request(url):
    try:
        response = requests.get(url, headers={'Content-Type':'application/json', 'Accept': 'application/json'})
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))

    except Exception as err:
        print('Other error occurred: {}'.format(err))

    else:
        return response.json()
    pass


def request_route():
    return(base_request(get_routes))

def request_stop(route, direction):
    url = get_stops.format(route,direction)

    return base_request(url)

def request_departure(route,direction,stop):
    url = get_timepoint.format(route,direction,stop)
    return(base_request(url))