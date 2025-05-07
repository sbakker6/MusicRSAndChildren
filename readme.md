# Project info

This project is part of the course CSE3500 Research Project of the Bachelor program of Computer Science and Engineering at the Delft University of Technology. 

In this project, we do an exploratory data analysis to analyze and try to uncover relations between extended musical features (i.e. song structure, artist information) and music listening behavior of children. 

The research paper is available at [TU Delft Repository](http://repository.tudelft.nl). 

We use a preprocessed version of the LastFM 2b dataset to do the analysis. 
This dataset contains around 2 billion listening events of users of the LastFm platform, including basic song and artist information and a timestamp at which the song was played by a particular user. 


# How to set up
- Download and install [Python](https://www.python.org/downloads/) if not yet installed (3.11.9 is used in this project)
- Create a [virtual environment](https://docs.python.org/3/library/venv.html) (recommended) and activate it
- Install the requirements `pip3 install -r requirements.txt` 
- Set `example-properties.properties` and rename to `properties.properties` 

# Recommended steps
### Create the SQLite database of the LFM-2b dataset.
Run `python3 lfm2b/db.py` to set up the SQLite database. This will take a long time. Required is the TSV data in the following structure in the lfm2b root folder (as specified in your properties.properties file)

```
|-artists_valid.tsv
|-tracks_valid.tsv
|-users_valid.tsv
|-listening-events.tsv
    |-listening-events.tsv
```

> I use the free software [DBeaver](https://dbeaver.io/) to connect to this database and query it.