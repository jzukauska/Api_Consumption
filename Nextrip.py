from Direction import Direction as D



class Nextrip():
    def __init__(self, user_route, user_stop, user_direction):
        self.__route = user_route
        self.__stop = user_stop
        self.__direction = self.__direction_convert(user_direction)

    def __direction_convert(self,value):
        lower = value.lower()
        try:
            direction_number = D[value].value
        except KeyError :
            print("Cardinal direction {} is not a valid direction".format(value))

        else:
            return(direction_number)





