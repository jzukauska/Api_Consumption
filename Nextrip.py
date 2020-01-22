from Direction import Direction as D

import json

from util import request_route


class Nextrip():
    def __init__(self, user_route, user_stop, user_direction):
        self.__route = user_route
        self.__stop = user_stop
        self.__direction = self.__direction_convert(user_direction)

    @staticmethod
    def __direction_convert(value):
        lower = value.lower()
        try:
            direction_number = D[lower].value
        except KeyError:
            print("Cardinal direction {} is not a valid direction".format(value))
            raise
        else:
            return direction_number

    @property
    def route(self):
        return self.__route

    def __get_routes(self):
        print("In get routes")
        routes_json_list = request_route()

        route_id = None
        for route in routes_json_list:

            if self.__route in route["Description"]:
                route_id = route["Route"]

        if route_id is None:
            raise ValueError("{} is not a vaild route".format(self.__route))

        else:
            print(route_id)
            return route_id

        pass

    def __get_stops(self):
        print("in get stops")
        self.__get_routes()
        pass

    def __get_departure(self):
        print("In getdeparture")
        self.__get_stops()

        pass

    def __str__(self):
        self.__get_departure()
        return ("Good")
