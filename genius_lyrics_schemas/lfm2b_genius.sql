DROP TABLE IF EXISTS lfm2b_genius;

CREATE TABLE lfm2b_genius (
   track_id INTEGER,
   song_id INTEGER,
   artist_confidence INTEGER,
   track_confidence INTEGER,
   PRIMARY KEY (track_id, song_id),
   FOREIGN KEY (song_id) REFERENCES song(song_id)
);

CREATE INDEX lfm2b_genius_track_id_idx ON lfm2b_genius(track_id);

CREATE INDEX lfm2b_genius_song_id_idx ON lfm2b_genius(song_id);