from jproperties import Properties
from pathlib import Path

# https://pypi.org/project/jproperties/
p = Properties()
with open("properties.properties", "rb") as f:
    p.load(f, "utf-8")

LYRICS_ROOT_FOLDER = Path(p['lyrics-root-folder'].data)
POSTGRES_CREDENTIALS = {
    "user" : p["postgres-username"].data,
    "password" : p["postgres-password"].data,
    "host" : p["postgres-host"].data,
    "port" : p["postgres-port"].data
}