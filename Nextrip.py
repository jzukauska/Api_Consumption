from Direction import Direction as D


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
        pass

    def __get_stops(self):
        pass

    def __getdeparture(self):

        pass

    def __str__(self):
        try:
            self.__getdeparture()

        finally:
            return ("Good")
