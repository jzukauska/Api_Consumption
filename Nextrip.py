from datetime import datetime

from Direction import Direction as D
from util import request_route, request_stop, request_departure


class Nextrip():
    def __init__(self, user_route: str, user_stop: str, user_direction: str):
        self.__route = user_route
        self.__stop = user_stop
        self.__direction = user_direction

        self.__api_route = ''
        self.__api_stop = ''
        self.__api_direction = self.__direction_convert(user_direction)

        self.__timestamp = None
        self.__departure = None

        self.__run_api_calls()

    @staticmethod
    def __direction_convert(value) -> int:
        lower = value.lower()
        try:
            direction_number = D[lower].value
        except KeyError:
            print("Cardinal direction '{}' is not a valid direction".format(value))
            raise
        else:
            return direction_number

    @property
    def route(self):
        return self.__route

    @property
    def stop(self):
        return self.__stop

    @property
    def direction(self):
        return self.__direction

    def __parse_route(self, json_route):

        for route in json_route:

            if self.__route in route["Description"]:
                return route["Route"]
        return None

    def __get_routes(self):
        routes_json_list = request_route()

        route_id = self.__parse_route(routes_json_list)

        if route_id is None:
            raise ValueError("'{}' is not a vaild route".format(self.__route))

        else:

            return route_id

        pass

    def __parse_stop(self, json_stop):

        for stop in json_stop:

            if self.__stop in stop["Text"]:
                return stop["Value"]
        return None

        pass

    def __get_stops(self):
        stops_json_list = request_stop(self.__api_route, self.__api_direction)

        stop_id = self.__parse_stop(stops_json_list)

        if stop_id is None:
            raise ValueError("'{}' and '{}' is not a vaild stop combination for '{}'"
                             .format(self.__route, self.__direction, self.__stop))

        else:

            return stop_id

        pass

    def __parse_departure(self, json_departure):
        # if there is something in the json array
        if json_departure:
            # todo check time zones
            dotnet_epoch_time_ms = json_departure[0]["DepartureTime"]
            departure_datetime = datetime.fromtimestamp(int(dotnet_epoch_time_ms[6:19]) / 1000)

            # edge case if time rolls over datetime in runtime to prevent rollover
            # if the time is that close the bus would pretty much be in sight
            if datetime.now() > departure_datetime:
                return 0

            datetime_difference = departure_datetime - datetime.now()

            return datetime_difference

    def __get_departure(self):
        departure_json_list = request_departure(self.__api_route, self.__api_direction, self.__api_stop)
        departure_time = self.__parse_departure(departure_json_list)

        return departure_time

        pass

    def __run_api_calls(self):
        self.__api_route = self.__get_routes()
        self.__api_stop = self.__get_stops()
        self.__departure = self.__get_departure()
        self.__timestamp = datetime.now()

    @property
    def timestamp(self):
        return self.__timestamp

    def __str__(self):

        if self.__departure is None:
            return ""
        else:
            mins = self.__departure.seconds // 60
            return "{} Minutes".format(mins)
