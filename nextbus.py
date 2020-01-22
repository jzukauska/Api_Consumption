import requests
import json
import pickle
from Nextrip import Nextrip
import argparse
import sys

debugMode = False

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

    bus = Nextrip(route,stop,direction)



