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