import unittest
from Nextrip import Nextrip as N

class TestNextTrip(unittest.TestCase):

    def test_user_input(self):
        # Assert error for incorrect direction input
        self.assertRaises(KeyError,N,"test","test","weast")

        pass