DROP TABLE IF EXISTS lyrics;

CREATE TABLE lyrics (
    song_id INTEGER PRIMARY KEY,
    lyrics TEXT,
    FOREIGN KEY (song_id) REFERENCES song(song_id)
);

