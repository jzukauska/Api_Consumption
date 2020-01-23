# Api_Consumption - nextbus - case study

Script utility that allows users to query their next bus arrival in minutes.

## Description

In a language of your choice, write a program which will tell you how long it is until the next bus on “BUS ROUTE”
 leaving from “BUS STOP NAME” going “DIRECTION” using the api defined at http://svc.metrotransit.org/ “BUS ROUTE” will
  be a substring of the bus route name which is only in one bus route “BUS STOP NAME” will be a substring of the bus
   stop name which is only in one bus stop on that route “DIRECTION” will be “north” “east” “west” or “south” 
## Getting Started

### Dependencies
* Python
  * Operating system that allows python to be installed and executed
  * `python` command reachable from terminal / command line
  * Python minimum version 3.4 compatible
  * See https://www.python.org/downloads/ for install instructions
* requests
  * Library used for making web requests
  * Ran from console or terminal, elevated user credentials may be required
  * ```
    pip install requests
    ```
* Deploying project to a python virtual environment is preferred but will not be covered
 in this document
##### *Optional*
* Git command line
  * https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  * Windows option: https://gitforwindows.org/
### Installing

* Download Zip Method
    * Download  https://github.com/jzukauska/Api_Consumption/archive/master.zip
    * Extract to your preferred folder
    * Navigate to that folder

* Git Method
  * open terminal or command line   
  * ```
    git clone https://github.com/jzukauska/Api_Consumption.git
    ```
  * ```
    cd Api_Consumption
    ```


### Executing program

* Ensure command line or terminal is open in directory that nextbus.py is available
    * Note the route, stop and direction arguments must each be surrounded in quotes
    * There are several responses that may be returned 
        * Blank line - Signifying no more buses in schedule 
        * X Minutes - Signifying time until next bus departure
        * Please wait X seconds before making a new request - Api update restriction per https://svc.metrotransit.org/nextrip docs
        * Error message - Helpful message to debug incorrect script input.
```
python nextbus.py "route" "stop" "direction"
```
* Examples
```
python nextbus.py "Express - Target - Hwy 252 and 73rd Av P&R - Mpls" "Target North Campus Building F" "south"

python nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"
139 Minutes

python nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"
Please wait 19 seconds before making a new request

python nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "weast"
Cardinal direction 'weast' is not a valid direction
KeyError: 'weast'
```
**WARNING**
* Use of the bypass [-b or --bypass] argument may lead to api restriction if abused 
```
python nextbus.py -b "METRO Blue Line" "Target Field Station Platform 1" "south"
139 Minutes
```
## Help

You can run `python nextbus.py -h` for a reminder
``` bash 
usage: nextbus.py [-h] [-b] route stop direction

Get next bus time

positional arguments:
  route         Substring of the bus route name
  stop          Substring of the bus stop name
  direction     North East West South

optional arguments:
  -h, --help    show this help message and exit
  -b, --bypass  WARNING bypass api overuse check, use at your own risk


```
## Test
* Test can be run with
  ```
  python -m unittest
  ```
* It requires that the test directory shipped with this repository be in the same directory you extracted nextbus.py to in order to test known relative directory schemas.



## Author
Jacob Zukauska 

