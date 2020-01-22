import unittest
from Nextrip import Nextrip as N
from Direction import Direction as D


class TestNextTrip(unittest.TestCase):

    def test_user_input(self):
        # Assert error for incorrect direction input
        self.assertRaises(KeyError, N._Nextrip__direction_convert(N, "weast"))

        bus_north = N("test", "test", "north")
        bus_south = N("test", "test", "south")
        bus_east = N("test", "test", "east")
        bus_west = N("test", "test", "west")
        self.assertEqual(bus_north._Nextrip__direction, D['north'].value)
        self.assertEqual(bus_south._Nextrip__direction, D["south"].value)
        self.assertEqual(bus_east._Nextrip__direction, D["east"].value)
        self.assertEqual(bus_west._Nextrip__direction, D["west"].value)

        pass

    def
