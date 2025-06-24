# LFM2b-GE dataset extension

The two presented tsv files serve as a link between the [LFM2b dataset](https://www.cp.jku.at/datasets/LFM-2b/) (unavailable for download as of June 2025), and the [Genius Expertise dataset](https://www.cs.cornell.edu/%7Earb/data/genius-expertise/) (GE).

This link is the outcome of a fuzzy matching process between the two datasets, which is part of this codebase. 

In `song.tsv`, IDs are provided to the songs in GE, along with the song URL and extracted artist and song name from the song URL. This file can be traced to `song_info.json` in GE.

In `lfm2b_genius.tsv`, we provide the link between these songs (with a 'song_id') and tracks in LFM2b (with a 'track_id'), along with a fuzzy matching score (from 0% to 100%) based on how well the artist and song name overlap in GE compared with LFM2b. 