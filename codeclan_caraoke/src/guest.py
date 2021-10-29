class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def cheer(self, songlist):
        if self.fav_song in songlist:
            return "Whohoo!!!"