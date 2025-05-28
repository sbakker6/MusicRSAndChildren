CREATE TABLE artist_genre (
    artist_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (artist_id, genre_id),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);