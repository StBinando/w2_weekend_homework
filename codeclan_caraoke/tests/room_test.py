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
        self.song1 = Song(songs[0]["title"], songs[0]["by"])
        self.song2 = Song(songs[1]["title"], songs[1]["by"])
        self.song3 = Song(songs[2]["title"], songs[2]["by"])
        self.song4 = Song(songs[3]["title"], songs[3]["by"])
        self.song5 = Song(songs[4]["title"], songs[4]["by"])
        self.song6 = Song(songs[5]["title"], songs[5]["by"])
        self.song7 = Song(songs[6]["title"], songs[6]["by"])
        self.song8 = Song(songs[7]["title"], songs[7]["by"])
        
        self.songlist1 = [self.song1, self.song2, self.song3, self.song4, self.song5]
        self.songlist2 = [self.song6, self.song7, self.song8]

        self.guest1 = Guest(guests[0])
        self.guest2 = Guest(guests[0])
        self.guest3 = Guest(guests[0])
        self.guest4 = Guest(guests[0])
        self.guest5 = Guest(guests[0])
        self.guest6 = Guest(guests[0])
        self.guest7 = Guest(guests[0])
        self.guest8 = Guest(guests[0])
        self.guest9 = Guest(guests[0])
        self.guest10 = Guest(guests[0])
        self.guest11 = Guest(guests[0])

        self.guestlist1 = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5]
        self.guestlist2 = [self.guest6, self.guest7, self.guest8]

        self.room1 = Room(room_names[0], self.guestlist1, self.songlist1)
        self.room2 = Room(room_names[1], [], self.songlist2)

    def test_room_has_name(self):
        self.assertEqual(self.room1.name, room_names[0])

    def test_room_has_guests(self):
        self.assertEqual(self.room1.guestlist, self.guestlist1)

    def test_room_is_empty(self):
        self.assertEqual(self.room2.guestlist, [])

    def test_room_has_songs(self):
        self.assertTrue(len(self.room2.songlist) > 0)

    def test_check_in_1_guest(self):
        self.assertEqual(len(self.room1.guestlist), 5)
        self.assertEqual(len(self.room2.guestlist), 0)
        self.room1.check_in_1_guest(self.guest9)
        self.room2.check_in_1_guest(self.guest10)
        self.assertEqual(len(self.room1.guestlist), 6)
        self.assertEqual(len(self.room2.guestlist), 1)

    def test_check_out_1_guest_ok(self):
        self.assertEqual(len(self.room1.guestlist), 5)
        self.room1.check_out_1_guest(self.guest3)
        self.assertEqual(len(self.room1.guestlist), 4)
    
    def test_check_out_1_guest_empty_room(self):
        self.assertEqual(len(self.room2.guestlist), 0)
        result = self.room2.check_out_1_guest(self.guest10)
        self.assertEqual(result, "this room is empty")

    def test_check_out_1_guest_is_not_here(self):
        self.assertEqual(len(self.room1.guestlist), 5)
        result = self.room1.check_out_1_guest(self.guest10)
        self.assertEqual(result, "guest not in this room")

    def test_check_out_all_guests_in_this_room(self):
        self.assertEqual(len(self.room1.guestlist), 5)
        self.room1.check_out_all_guests_in_this_room()
        self.assertEqual(len(self.room1.guestlist), 0)

    def test_check_out_all_guests_in_empty_room(self):
        self.assertEqual(len(self.room2.guestlist), 0)
        result = self.room2.check_out_all_guests_in_this_room()
        self.assertEqual(result, "this room is already empty")

    def test_add_song_to_room(self):
        self.assertEqual(len(self.room1.songlist), 5)
        self.room1.add_song_to_room(self.song6)
        self.assertEqual(len(self.room1.songlist), 6)
        
