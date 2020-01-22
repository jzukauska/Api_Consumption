from datetime import datetime

import requests
import json
import pickle
from Nextrip import Nextrip
import argparse
import sys
from os import path


debugMode = True

if not debugMode:
    sys.tracebacklimit = 0



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get next bus time')
    parser.add_argument('route', type=str, help='Substring of the bus route name')
    parser.add_argument('stop', type=str, help='Substring of the bus stop name')
    parser.add_argument('direction', type=str, help='"North” “East” “West” or “South”')

    args = parser.parse_args()

    route = args.route
    stop = args.stop
    direction = args.direction

    bus_time = Nextrip(route,stop,direction)

    print(bus_time)

    # cache = None
    # if path.exists("./cache") and path.getsize("./cache") > 0:
    #     try:
    #         cache = pickle.load(open("cache","rb"))
    #     except:
    #         print("Error loading cache")
    #
    # if cache is not None:
    #     if (cache.timestamp - datetime.now()).seconds < 30:
    #         print("Under 30")
    #
    #


