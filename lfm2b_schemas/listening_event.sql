CREATE TABLE listening_event (
    user_id INTEGER,
    track_id INTEGER,
    timestamp_listen TEXT,
    age_at_listen INTEGER,
    artist_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES lfm_user(user_id),
    FOREIGN KEY (track_id) REFERENCES track(track_id),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);