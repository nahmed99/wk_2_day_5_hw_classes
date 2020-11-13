class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

        self.guests = []
        self.songs = []


    def guest_count(self):
        return len(self.guests)

    # def check_in(self, new_guest):
    #     self.guest