import unittest
from src.room import Room

# Declaration of values to be used for tests
room_names = ["Rock", "Pop", "Punk", "Jazz", "Hard Rock", "Bossa Nova"]
guests = ["Mike", "Tom", "Susan", "Kate", "David", "Alex", "Robert", "Zoe", "Louise", "George", "Heather"]
songs = [
    {
        "title" : "Five Years",
        "by" : "David Bowie"
    },
    {
        "title" :"Kill the poor",
        "by" : "Dead Kennedys"
    },
    {
        "title" :"Sea and Sand",
        "by" : "Nicola Conte"
    },
    {
        "title" :"Águas de Março",
        "by" : "Tom Jobim"
    },
    {
        "title" :"Hells Bells",
        "by" : "AC/DC"
    },
    {
        "title" :"Paparazzi",
        "by" : "Lady Gaga"
    }
]


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(room_names[0], guests[0:5], songs[0:3])
        self.room2 = Room(room_names[1], [], songs[4:5])

    def test_room_has_name(self):
        self.assertEqual(self.room1.name, room_names[0])

    def test_room_has_guests(self):
        self.assertEqual(self.room1.guests, guests[0:5])

    def test_room_is_empty(self):
        self.assertEqual(self.room2.guests, [])

    def test_room_has_songs(self):
        self.assertTrue(len(self.room2.songs) > 0)
