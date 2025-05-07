CREATE TABLE lfm_user (
    user_id INTEGER,
    gender CHAR(1),
    country TEXT(2),
    creation_time TEXT,
    age_on_2013_10_31 INTEGER,
    age_valid BOOLEAN,
    PRIMARY KEY (user_id)
);