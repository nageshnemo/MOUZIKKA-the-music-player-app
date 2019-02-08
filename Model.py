import sqlite3
class Model:

    def __init__(self):
        self.song_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None
        try:
            self.conn = sqlite3.connect("MOUZIKA.db")
            print("Connected successfully to the DB")
            self.cur = self.conn.cursor()

        except DatabaseError:
            self.db_status = False

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Cursor closed successfully")
        if self.conn is not None:
            self.conn.close()
            print("Disconnected successfully from the DB")

    def add_song(self, song_name, song_path):
        self.song_dict[song_name] = song_path
        print("song added:", self.song_dict[song_name])

    def get_song_path(self, song_name):
        return self.song_dict[song_name]

    def remove_song(self, song_name):
        self.song_dict.pop(song_name)
        print(self.song_dict)

    def search_song_in_favourites(self, song_name):
        pass

    def add_song_from_favourites(self, song_name, song_path):
        pass

    def load_songs_from_favourites(self):
        pass

