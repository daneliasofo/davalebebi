class MusicBox:
    def __init__(self, box_name):
        self.box_name = box_name
        self.songs = []


box = MusicBox("My Playlist")

box.songs.append("century")
box.songs.append("4 raws")
box.songs.append("massive")

box.songs.remove("massive")

print("სიმღერები:", box.songs)