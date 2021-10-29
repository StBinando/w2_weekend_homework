import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

# Declaration of values to be used for tests
room_names = ["Rock", "Pop", "Punk", "Jazz", "Hard Rock", "Bossa Nova"]
guests = ["Mike", "Tom", "Susan", "Kate", "David", "Alex", "Robert", "Zoe", "Louise", "George", "Heather"]
songs = [
    { # song 1
        "title" : "Five Years", 
        "by" : "David Bowie"
    },
    { # song 2
        "title" : "Kill the poor",
        "by" : "Dead Kennedys"
    },
    { # song 3
        "title" : "Sea and Sand",
        "by" : "Nicola Conte"
    },
    { # song 4
        "title" : "Águas de Março",
        "by" : "Tom Jobim"
    },
    { # song 5
        "title" : "Just like heaven",
        "by" : "The Cure"
    },
    { # song 6
        "title" : "Hells Bells",
        "by" : "AC/DC"
    },
    { # song 7
        "title" : "Paparazzi",
        "by" : "Lady Gaga"
    },
    { # song 8
        "title" : "Just like heaven",
        "by" : "Katie Melua"
    }
    
]


class TestRoom(unittest.TestCase):
    def setUp(self):
        song1 = Song(songs[0]["title"], songs[0]["by"])
        song2 = Song(songs[1]["title"], songs[1]["by"])
        song3 = Song(songs[2]["title"], songs[2]["by"])
        song4 = Song(songs[3]["title"], songs[3]["by"])
        song5 = Song(songs[4]["title"], songs[4]["by"])
        song6 = Song(songs[5]["title"], songs[5]["by"])
        song7 = Song(songs[6]["title"], songs[6]["by"])
        song8 = Song(songs[7]["title"], songs[7]["by"])
        
        songlist1 = [song1, song2, song3, song4, song5]
        songlist2 = [song6, song7, song8]

        guest1 = Guest(guests[0])
        guest2 = Guest(guests[0])
        guest3 = Guest(guests[0])
        guest4 = Guest(guests[0])
        guest5 = Guest(guests[0])
        guest6 = Guest(guests[0])
        guest7 = Guest(guests[0])
        guest8 = Guest(guests[0])
        guest9 = Guest(guests[0])
        guest10 = Guest(guests[0])
        guest11 = Guest(guests[0])

        self.guestlist1 = [guest1, guest2, guest3, guest4, guest5]
        self.guestlist2 = [guest6, guest7, guest8]

        self.room1 = Room(room_names[0], self.guestlist1, songlist1)
        self.room2 = Room(room_names[1], [], songlist2)

    def test_room_has_name(self):
        self.assertEqual(self.room1.name, room_names[0])

    def test_room_has_guests(self):
        self.assertEqual(self.room1.guestlist, self.guestlist1)

    def test_room_is_empty(self):
        self.assertEqual(self.room2.guestlist, [])

    def test_room_has_songs(self):
        self.assertTrue(len(self.room2.songlist) > 0)

    
