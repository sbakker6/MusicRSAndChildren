from jproperties import Properties
from pathlib import Path

# https://pypi.org/project/jproperties/
p = Properties()
with open("properties.properties", "rb") as f:
    p.load(f, "utf-8")

LFM2B_ROOT = Path(p["lfm2b-root-folder"].data)
LFM2B_ENHANCED_ROOT = Path(p["lfm2b-enhanced-root-folder"].data)
LFM2B_DB = Path(LFM2B_ROOT, p["lfm2b-db"].data)
LFM2B_ENHANCED_DB = Path(LFM2B_ENHANCED_ROOT, p["lfm2b-enhanced-db"].data)
LOG_PATH = Path(LFM2B_ROOT, p["logfile"].data)
CSV_FOLDER = Path(p["csv-root-folder"].data)
LYRICS_ROOT_FOLDER = Path(p['lyrics-root-folder'].data)
GENIUS_DB = Path(LYRICS_ROOT_FOLDER, p["genius-db"].data)