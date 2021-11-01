class Room:
    def __init__(self, name, guestlist, songlist, capacity):
        self.name = name
        self.guestlist = guestlist
        self.songlist = songlist
        self.capacity = capacity

    
    def check_in_1_guest(self, guest):
        if len(self.guestlist) == self.capacity:
            return "sorry, this room is full"
        self.guestlist.append(guest)

    # The following method removes a specific value, if present, from the list "guestlist"
    def check_out_1_guest(self, guest): 
        if len(self.guestlist) == 0: # checks that the list is not empty
            return "this room is empty" # if it is empty returns a message
        elif not(guest in self.guestlist): # checks that a specific value is in the list
            return "guest not in this room" # it the value is not present returns a message
        self.guestlist.remove(guest) # with both conditions satisfied, the guest gets removed from the list

    def check_out_all_guests_in_this_room(self):
        if len(self.guestlist) == 0:
            return "this room is already empty"
        self.guestlist.clear()

    def add_song_to_room(self, song):
        if song in self.songlist:
            return "song already in this room"
        self.songlist.append(song)

