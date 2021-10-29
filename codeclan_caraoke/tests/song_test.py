import unittest
from src.song import Song

# Declaration of values to be used for tests
songs = [
    {
        "title" : "Five Years",
        "by" : "David Bowie"
    },
    {
        "title" : "Kill the poor",
        "by" : "Dead Kennedys"
    },
    {
        "title" : "Sea and Sand",
        "by" : "Nicola Conte"
    },
    {
        "title" : "Águas de Março",
        "by" : "Tom Jobim"
    },
    {
        "title" : "Hells Bells",
        "by" : "AC/DC"
    },
    {
        "title" : "Paparazzi",
        "by" : "Lady Gaga"
    },
    {
        "title" : "Just like heaven",
        "by" : "The Cure"
    },
    {
        "title" : "Just like heaven",
        "by" : "Katie Melua"
    }
    
]
class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song(songs[0]["title"], songs[0]["by"])
        self.song2 = Song(songs[1]["title"], songs[1]["by"])
        self.song3 = Song(songs[2]["title"], songs[2]["by"])
        self.song4 = Song(songs[3]["title"], songs[3]["by"])
        self.song5 = Song(songs[4]["title"], songs[4]["by"])
        self.song6 = Song(songs[5]["title"], songs[5]["by"])
        self.song7 = Song(songs[6]["title"], songs[6]["by"])
        self.song8 = Song(songs[7]["title"], songs[7]["by"])

        # print(f'"{self.song7.title}" by {self.song7.by}')


    def test_songs_have_titles(self):
        self.assertTrue(self.song1.title, songs[0]["title"])
        self.assertTrue(self.song2.title, songs[1]["title"])

    def test_songs_have_bys(self):
        self.assertTrue(self.song1.title, songs[0]["by"])
        self.assertTrue(self.song2.title, songs[1]["by"])

    
