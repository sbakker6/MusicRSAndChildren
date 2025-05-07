from jproperties import Properties
from pathlib import Path

# https://pypi.org/project/jproperties/
p = Properties()
with open("properties.properties", "rb") as f:
    p.load(f, "utf-8")

LFM2B_ROOT = Path(p["lfm2b-root-folder"].data)
LFM2B_DB = Path(LFM2B_ROOT, p["lfm2b-db"].data)
LOG_PATH = Path(LFM2B_ROOT, p["logfile"].data)