# Project info

This repository links to the work of students for the Research project course (edition of 2025) of the CSE bachelor at TU Delft.
Please see their projects [here](https://cse3000-research-project.github.io/).

In this project, we perform data analysis to uncover potential relations between extended song structure and music listening behavior of children. 
For all songs in a combined dataset we calculate a structural fingerprint based on song sections, which are extracted from the songs' lyrics. Using k-means clustering, we identify groups of songs, structures, with similar fingerprints. Then, we examine how these different structures are represented in the listening behavior of children in two age groups (12-14, 15-17) and adults (18-64). 

The research paper is available at [TU Delft Repository](http://repository.tudelft.nl). 

We use a preprocessed version of the LastFM 2b (LFM2b) dataset from the paper [The Impact of Mainstream-Driven Algorithms on Recommendations for Children](https://link.springer.com/chapter/10.1007/978-3-031-88714-7_5) by R. Ungruh, A. Bellogin and M.S. Pera to do the analysis and match it with the [Genius-Expertise](https://www.cs.cornell.edu/%7Earb/data/genius-expertise/) (GE) dataset.

This repository contains
- the code used to produce the linkage between LFM2b and GE;
- the code used to extract structure fingerprints from lyrics;
- figures (inclusive the code to create them) used in the paper
- the final LFM2b-GE linkage (in the `datafiles` directory)

>**!!** This repository does **not** distribute the LFM2b dataset, as it is not available for download anymore due to [licensing issues](https://www.cp.jku.at/datasets/LFM-2b/) (as of June 2025). Despite this, those who already poses the dataset can use it to reproduce the analysis and can use the LFM2b-GL linkage out of the box. 

# How to set up

### Python environment
- Download and install [Python](https://www.python.org/downloads/) if not yet installed (3.11.9 is used in this project)
- Create a [virtual environment](https://docs.python.org/3/library/venv.html) (recommended) and activate it
- Install the requirements `pip3 install -r requirements.txt` 
> VSCode was used to interact with Jupyter Notebooks, so the requirements contain VSCode specific packages


### Postgres Database
<!-- Run `python3 lfm2b/db.py` to set up the SQLite database. This will take a long time. Required is the TSV data in the following structure in the lfm2b root folder (as specified in your properties.properties file)

```
|-artists_valid.tsv
|-tracks_valid.tsv
|-users_valid.tsv
|-listening-events.tsv
    |-listening-events.tsv
``` -->

A PostgreSQL database in a [Docker](https://www.docker.com) container was used in this project on a **Postgres 17** image.

The Postgres server should contain the LFM2b database with the name "lfm2b" and schemas as layed out in `lfm2b/lfm2b_schemas`.

> [DBeaver](https://dbeaver.io/) can be used as a free database tool.

### Properties file

The code works through a properties file, which contains database credentials
and the locations for certain files. 

Fill the `example-properties.properties` file with the correct data and rename it to `properties.properties`. 



