CREATE TABLE track (
    track_id INTEGER,
    track_name TEXT,
    artist_id INTEGER,
    PRIMARY KEY (track_id),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);