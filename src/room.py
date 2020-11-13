class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

        self.guests = []
        self.songs = []


    def guest_count(self):
        return len(self.guests)


    def check_in(self, new_guest):
        self.guests.append(new_guest)


    def check_out(self, guest_name):
        for guest in self.guests:
            if guest.name == guest_name:
                return guest


    def song_count(self):
        return len(self.songs)


    def add_song(self, new_song):
        self.songs.append(new_song)