import csv
import logging
from pathlib import Path
import sqlite3
from properties import LFM2B_ROOT, LFM2B_DB


logging.basicConfig(filename='db_creation.log', level=logging.INFO, datefmt='%d-%m-%Y,%H:%M:%S',
                    format='%(levelname)s - %(asctime)s: %(message)s')
LOGGER = logging.getLogger()

# Tables in order of creation (this order respects foreign keys)
tables = [
    ("artist", "artist.sql"),
    ("genre", "genre.sql"),
    ("artist_genre", "artist_genre.sql"),
    ("lfm_user", "user.sql"),
    ("track", "track.sql"),
    ("listening_event", "listening_event.sql")
]


def delete_all(db_cursor):
    """Deletes all data from the database. Does not commit."""
    for table, _ in reversed(tables):
        db_cursor.execute(f"DROP TABLE IF EXISTS {table}")


def create_database(db_cursor):
    """Runs all the SQL create table files. Does not commit."""
    for _, file_name in tables:
        with open(Path("lfm2b_schemas", file_name), 'r', encoding='utf-8') as f:
            db_cursor.execute(f.read())


def populate_artists_and_genres(db_cursor):
    """
    Goes through `artists_valid.tsv` and populates tables `artist`, `genre` and `artist_genre`.
    Output is logged to db_creation.log
    """
    processed_genres = set()
    id_of_genre = {}

    num_errors = 0
    with open(Path(LFM2B_ROOT, "artists_valid.tsv"), 'r', encoding='utf-8') as f:
        LOGGER.info("---- ARTIST-AND-GENRES")
        reader = create_reader(f)
        for i, row in enumerate(reader):
            try:
                artist_id, artist_name, genres = row
                # Add the artist
                db_cursor.execute("INSERT OR IGNORE INTO artist VALUES (?, ?)", [artist_id, artist_name])
                for genre in [g.strip() for g in genres.split(",")]:
                    # Add the genre to the genre table
                    if genre not in processed_genres:
                        processed_genres.add(genre)
                        id_of_genre[genre] = len(processed_genres)
                        db_cursor.execute("INSERT INTO genre VALUES (?, ?)", [id_of_genre[genre], genre])
                    # Add the link of artist and genre to the join table
                    db_cursor.execute("INSERT OR IGNORE INTO artist_genre VALUES (?, ?)",
                                      [artist_id, id_of_genre[genre]])  # IGNORE makes sure to not allow duplicates
            except Exception as err:
                LOGGER.error("row_no: %d. row : %s. err : %s", i, row, err)
                num_errors += 1
                continue
        LOGGER.info("#artists written: %d", db_cursor.execute("SELECT count(*) FROM artist").fetchone()[0])
        LOGGER.info("#genres written: %d", db_cursor.execute("SELECT count(*) FROM genre").fetchone()[0]),
        LOGGER.warning('#errors: %d', num_errors)
        LOGGER.info("---- ARTIST-AND-GENRES")


def populate_tracks(db_cursor, start=None, end=None):
    """
    Goes through `tracks_valid.tsv` and populates table `track`.
    Output is logged to db_creation.log

    start and end indicate the rows that should be considered (0-indexed, inclusive bounds)
    """
    num_errors = 0
    start_tracks = db_cursor.execute("SELECT count(*) FROM track").fetchone()[0]
    with open(Path(LFM2B_ROOT, "tracks_valid.tsv"), 'r', encoding='utf-8') as f:
        LOGGER.info("---- TRACKS")
        LOGGER.info("start=%s, end=%s", start, end)
        reader = create_reader(f)
        next(reader)  # this file contains headers
        for i, row in enumerate(reader):
            if end is not None and i > end:
                break
            if start is not None and i < start:
                continue

            try:
                track_id, track_name, artist_id = row
                db_cursor.execute("INSERT INTO track VALUES (?, ?, ?)", [track_id, track_name, artist_id])
            except Exception as err:
                LOGGER.error("row_no: %d. row : %s. err : %s", i, row, err)
                num_errors += 1
                continue
        LOGGER.info("#tracks written: %d", db_cursor.execute("SELECT count(*) FROM track").fetchone()[0] - start_tracks)
        LOGGER.warning('#errors: %d', num_errors)
        LOGGER.info("---- TRACKS")


def populate_users(db_cursor):
    """
    Goes through `users_valid.tsv` and populates table `lfm_user`.
    Output is logged to db_creation.log
    """
    num_errors = 0
    with open(Path(LFM2B_ROOT, "users_valid.tsv"), 'r', encoding='utf-8') as f:
        LOGGER.info("---- USERS")
        reader = create_reader(f)
        for i, row in enumerate(reader):
            try:
                user_id, gender, country, creation_time, age_on_2013_10_31, age_valid = row
                db_cursor.execute("INSERT INTO lfm_user VALUES (?, ?, ?, ?, ?, ?)",
                                  [user_id, gender, country, creation_time, age_on_2013_10_31, age_valid])
            except Exception as err:
                LOGGER.error("row_no: %d. row : %s. err : %s", i, row, err)
                num_errors += 1
                continue
        LOGGER.info("#users written: %d", db_cursor.execute("SELECT count(*) FROM lfm_user").fetchone()[0])
        LOGGER.warning('#errors: %d', num_errors)
        LOGGER.info("---- USERS")


def populate_listening_events(db_cursor):
    """
    Goes through `listening-events.tsv` and populates table `listening_event`.
    Output is logged to db_creation.log
    """
    num_errors = 0
    with open(Path(LFM2B_ROOT, "listening-events.tsv", "listening-events.tsv"), 'r', encoding='utf-8') as f:
        LOGGER.info("---- LISTENING EVENTS")
        reader = create_reader(f)
        for i, row in enumerate(reader):
            try:
                user_id, track_id, timestamp, age_at_listen, artist_id = row
                db_cursor.execute("INSERT INTO listening_event VALUES (?, ?, ?, ?, ?)",
                                  [user_id, track_id, timestamp, age_at_listen, artist_id])
            except Exception as err:
                LOGGER.error("row_no: %d. row : %s. err : %s", i, row, err)
                num_errors += 1
                continue
        LOGGER.info("#LEs written: %d", db_cursor.execute("SELECT count(*) FROM listening_event").fetchone()[0])
        LOGGER.warning('#errors: %d', num_errors)
        LOGGER.info("---- LISTENING EVENTS")


def populate_database(db_cursor):
    """Reads files and fills the database """
    populate_artists_and_genres(db_cursor)
    populate_tracks(db_cursor, start=None, end=None)
    populate_users(db_cursor)
    populate_listening_events(db_cursor)


def create_reader(file):
    return csv.reader(file, delimiter="\t")


def main():
    print("Creating database...")
    con = sqlite3.connect(LFM2B_DB)
    cursor = con.cursor()
    delete_all(cursor)
    create_database(cursor)
    populate_database(cursor)
    con.commit()
    print("Done!")
    con.close()


if __name__ == '__main__':
    main()
