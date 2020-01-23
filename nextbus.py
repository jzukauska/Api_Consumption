import argparse
import pickle
import sys
from datetime import datetime
from os import path

from Nextrip import Nextrip

debugMode = False

if not debugMode:
    sys.tracebacklimit = 0

COOL_DOWN_TIME = 30

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get next bus time')
    parser.add_argument('route', type=str, help='Substring of the bus route name')
    parser.add_argument('stop', type=str, help='Substring of the bus stop name')
    parser.add_argument('direction', type=str, help='North East West South')
    parser.add_argument('-b', '--bypass', action="store_true",
                        help="WARNING bypass api overuse check, use at your own risk")

    args = parser.parse_args()

    route = args.route
    stop = args.stop
    direction = args.direction
    bypass = args.bypass

    if not path.isfile("./cache"):
        with open("./cache", "wb"):
            bus_time = Nextrip(route, stop, direction)

            print(bus_time)
            pickle.dump(bus_time, open("./cache", 'wb'))

    else:
        with open("./cache", "rb") as f:
            cached_bus = pickle.load(f)
            if (datetime.now() - cached_bus.timestamp).seconds < COOL_DOWN_TIME and not bypass:
                if cached_bus.direction == direction and cached_bus.route == route and cached_bus.stop == stop:
                    print(cached_bus)
                else:
                    time_left = COOL_DOWN_TIME - (datetime.now() - cached_bus.timestamp).seconds
                    print("Please wait {} seconds before making a new request".format(time_left))
            else:
                bus_time = Nextrip(route, stop, direction)

                print(bus_time)
                pickle.dump(bus_time, open("./cache", 'wb'))
