import requests
import json
import pickle
import Nextrip

if __name__ == '__main__':
    response = (requests.get('https://api.github.com'))
    print(response.status_code)
