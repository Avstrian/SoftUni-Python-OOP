from project.song import Song


class Album:

    def __init__(self, name, songs=None):
        self.name = name
        if songs is None:
            self.songs = []
        else:
            self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        info = f"Album {self.name}\n"
        for song in self.songs:
            info += f"{song.get_info()}\n"
        return info
