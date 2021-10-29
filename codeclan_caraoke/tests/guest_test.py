import unittest
from src.guest import Guest
from src.song import Song

# Declaration of values to be used for tests
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



class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song(songs[0]["title"], songs[0]["by"])
        self.song2 = Song(songs[1]["title"], songs[1]["by"])
        self.song3 = Song(songs[2]["title"], songs[2]["by"])
        self.song4 = Song(songs[3]["title"], songs[3]["by"])
        self.song5 = Song(songs[4]["title"], songs[4]["by"])
        self.song6 = Song(songs[5]["title"], songs[5]["by"])
        self.song7 = Song(songs[6]["title"], songs[6]["by"])
        self.song8 = Song(songs[7]["title"], songs[7]["by"])
        
        self.guest1 = Guest(guests[0], 10, self.song1)
        self.guest2 = Guest(guests[1], 20, self.song6)
        self.guest3 = Guest(guests[2], 15, self.song8)
        self.guest4 = Guest(guests[3], 50, self.song3)
        self.guest5 = Guest(guests[4], 5, self.song2)
        self.guest6 = Guest(guests[5], 25, self.song7)
        self.guest7 = Guest(guests[6], 33, self.song4)
        self.guest8 = Guest(guests[7], 12, self.song1)
        self.guest9 = Guest(guests[8], 27, self.song5)
        self.guest10 = Guest(guests[9], 100, self.song6)
        self.guest11 = Guest(guests[10], 18, self.song2)

    def test_guest_has_name(self):
        self.assertEqual(self.guest1.name, guests[0])
