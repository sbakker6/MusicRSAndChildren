from models import SongStructure

class Song:
    ID = 0
    def __init__(self, genius_url, title, artist, lyrics):
        self.id = Song.ID
        Song.ID += 1
        self.genius_url = genius_url
        self.title : str = title
        self.artist : str = artist
        self.lyrics : str = lyrics
    
    def __repr__(self):
        return f"{self.artist} - {self.title}"
    
    def extract_structure(self, structure_strategy) -> SongStructure :
        return structure_strategy(self.lyrics)