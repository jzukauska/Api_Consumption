import unittest
from Nextrip import Nextrip as N
import datetime


class TestNextTrip(unittest.TestCase):

    def test_user_input(self):
        # Assert error for incorrect direction input


        with self.assertRaises(KeyError):
            N("test","test","weast")
        pass

    def test_output(self):

        #assuming good cardinal direction


        badroute = "badroute"
        badstring = "'{}' is not a vaild route".format(badroute)
        with self.assertRaises(ValueError) as context:
            N(badroute, "test", "north")

        self.assertTrue(badstring in str(context.exception))


        #valid route and direction but stop is invalid
        badstop = "badstop"
        badstopstring = "'{}' and '{}' is not a vaild stop combination for '{}'".format("METRO Blue Line","south", badstop )
        with self.assertRaises(ValueError) as context:
            N("METRO Blue Line", badstop, "south")

        self.assertTrue(badstopstring in str(context.exception))

    def test_timestamp(self):
        bus = N("METRO Blue Line", "Target Field Station Platform 1", "south")

        self.assertIsNotNone(bus.timestamp)
        self.assertIs(type(bus.timestamp), datetime.datetime)

