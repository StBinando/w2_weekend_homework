import unittest
from src.guest import Guest

# Declaration of values to be used for tests
guests = ["Mike", "Tom", "Susan", "Kate", "David", "Alex", "Robert", "Zoe", "Louise", "George", "Heather"]

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest(guests[0])
        self.guest2 = Guest(guests[1])
        self.guest3 = Guest(guests[2])
        self.guest4 = Guest(guests[3])
        self.guest5 = Guest(guests[4])
        self.guest6 = Guest(guests[5])
        self.guest7 = Guest(guests[6])
        self.guest8 = Guest(guests[7])
        self.guest9 = Guest(guests[8])
        self.guest10 = Guest(guests[9])
        self.guest11 = Guest(guests[10])

    def test_guest_has_name(self):
        self.assertEqual(self.guest1.name, guests[0])
