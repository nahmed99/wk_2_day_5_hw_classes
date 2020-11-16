class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        
        self.guests = []
        self.songs = []


    def guest_count(self):
        return len(self.guests)


    def check_in(self, new_guest):
        if self.check_capacity() and self.confirm_guest_has_funds(new_guest):
            # You should take fee from the guest at this point too!!!
            ##### self.take_fee_from_guest(new_guest)
            self.guests.append(new_guest)


    def check_out(self, guest_name):
        for guest in self.guests:
            if guest.name == guest_name:
                return guest


    def song_count(self):
        return len(self.songs)


    def add_song(self, new_song):
        self.songs.append(new_song)


    def check_capacity(self):
        # return True if there is room for more guests
        return self.guest_count() < self.capacity


    def confirm_guest_has_funds(self, guest):
        # return True if guest has sufficient funds to pay entry fee
        return guest.money >= self.entry_fee

    
    def take_fee_from_guest(self, guest):
        # Should you really have the following if in this function? See function check_im above.
        if self.confirm_guest_has_funds(guest):
            guest.money -= self.entry_fee


    def look_for_guest_fav_song(self, guest):
        for song in self.songs:
            if song.name == guest.fav_song:
                return "Whoo!"
