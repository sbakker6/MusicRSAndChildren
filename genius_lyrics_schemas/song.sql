DROP TABLE IF EXISTS song;

CREATE TABLE song (
    song_id INTEGER,
    genius_url TEXT,
    artist_name TEXT,
    song_name TEXT,
    PRIMARY KEY (song_id)
);

CREATE INDEX song_song_id_idx ON song(song_id); 