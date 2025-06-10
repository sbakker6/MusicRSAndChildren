DROP TABLE IF EXISTS song_cluster;

CREATE TABLE song_cluster (
    song_id INTEGER,
    cluster_id INTEGER,
    PRIMARY KEY (song_id, cluster_id),
    FOREIGN KEY (song_id) REFERENCES song(song_id),
    FOREIGN KEY (cluster_id) REFERENCES cluster(cluster_id)
);

CREATE INDEX  ON song_cluster(cluster_id); 

CREATE INDEX  ON song_cluster(song_id); 