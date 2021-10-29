class Room:
    def __init__(self, name, guestlist, songlist):
        self.name = name
        self.guestlist = guestlist
        self.songlist = songlist

    def check_in_1_guest(self, guest):
        self.guestlist.append(guest)

    def check_out_1_guest(self, guest):
        if len(self.guestlist) == 0:
            return "this room is empty"
        elif not(guest in self.guestlist):
            return "guest not in this room"
        self.guestlist.remove(guest)

    def check_out_all_guests_in_this_room(self):
        if len(self.guestlist) == 0:
            return "this room is already empty"
        self.guestlist.clear()

    def add_song_to_room(self, song):
        if song in self.songlist:
            return "song already in this room"
        self.songlist.append(song)

