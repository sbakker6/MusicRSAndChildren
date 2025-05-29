DROP TABLE IF EXISTS cluster;

CREATE TABLE cluster (
    song_id INTEGER PRIMARY KEY,
    cluster_id INTEGER,
    FOREIGN KEY (song_id) REFERENCES song(song_id)
);

CREATE INDEX  ON cluster(cluster_id); 