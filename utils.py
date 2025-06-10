import os
from pathlib import Path
import psycopg2
from properties import POSTGRES_CREDENTIALS


def create_connection(db_name):
    """ Create a connection to the postgres database. Returns a tuple of (connection, cursor) for convenience"""
    connection = psycopg2.connect(dbname=db_name, **POSTGRES_CREDENTIALS)
    return (connection, connection.cursor())

def execute_script(script_path, cursor):
    """ Execute an SQL script """
    with open(script_path, "r") as script_file:
       script = script_file.read().strip()
       cursor.execute(script)

def find_first(pred, iterable):
    """ Find first element of the iterable satisfying the predicate. If no match is found, returns None"""
    for e in iterable:
        if pred(e):
            return e
    return None

def song_filter_id(id : int):
    return lambda song : song.id == id

def make_folder_if_not_exists(fname : Path):
    if not os.path.exists(fname):
        os.makedirs(fname)
    return fname