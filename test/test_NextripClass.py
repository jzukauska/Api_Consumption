import unittest
from Nextrip import Nextrip as N
from Direction import Direction as D


class TestNextTrip(unittest.TestCase):

    def test_user_input(self):
        # Assert error for incorrect direction input


        with self.assertRaises(KeyError):
            N("test","test","weast")

        bus_north = N("test", "test", "noRth")
        bus_south = N("test", "test", "sOUth")
        bus_east = N("test", "test", "East")
        bus_west = N("test", "test", "WEST")
        self.assertEqual(bus_north._Nextrip__direction, D['north'].value)
        self.assertEqual(bus_south._Nextrip__direction, D["south"].value)
        self.assertEqual(bus_east._Nextrip__direction, D["east"].value)
        self.assertEqual(bus_west._Nextrip__direction, D["west"].value)

        pass

    def test_output(self):
        #assuming good cardinal direction
        with self.assertRaises(ValueError):
            N("test","test","north")._Nextrip__get_routes()
