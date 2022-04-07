CREATE TABLE role(
    role VARCHAR(20),
     PRIMARY KEY (role)
);

CREATE TABLE player(
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(20),
    surname VARCHAR(20),
    birth_date DATE,
    nationality VARCHAR(20),
    height INTEGER,
    role VARCHAR(20),
    FOREIGN KEY (role) REFERENCES role(role),
    PRIMARY KEY (id)
);

CREATE TABLE coach(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(20),
    surname VARCHAR(20),
    birth_date DATE,
    nationality VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE referee(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(20),
    surname VARCHAR(20),
    birth_date DATE,
    nationality VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE referee_stats(
    nr_matches INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    referee_id INTEGER,
    FOREIGN KEY (referee_id) REFERENCES referee(id)
);


CREATE TABLE season(
    start_year DATE,
    end_year DATE,
    PRIMARY KEY (start_year, end_year)
);

CREATE TABLE matches(
    id INTEGER NOT NULL AUTO_INCREMENT,
    home VARCHAR(20),
    away VARCHAR(20),
    day DATE,
    result VARCHAR(5),
    season_start DATE,
    season_end DATE,
    PRIMARY KEY (id)
);

CREATE TABLE team(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(20),
    address VARCHAR(100),
    stadium VARCHAR(20),
    url VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE team_coach(
    coach_id INTEGER,
    team_id INTEGER,
    season_start DATE,
    season_end DATE,
    FOREIGN KEY (season_start, season_end) REFERENCES season(start_year,end_year),
    FOREIGN KEY (coach_id) REFERENCES coach(id),
    FOREIGN KEY (team_id) REFERENCES team(id),
    PRIMARY KEY (team_id, coach_id)
);

CREATE TABLE team_player(
    player_id INTEGER,
    team_id INTEGER,
    season_start DATE,
    season_end DATE,

    FOREIGN KEY (season_start, season_end) REFERENCES season(start_year,end_year),
    FOREIGN KEY (player_id) REFERENCES coach(id),
    FOREIGN KEY (team_id) REFERENCES team(id),
    PRIMARY KEY (team_id, player_id)
);

CREATE TABLE results(
   result VARCHAR(5),
   match_id INTEGER,
   FOREIGN KEY (match_id) REFERENCES matches(id),
   PRIMARY KEY (result)
);

CREATE TABLE team_season(
    team_id INTEGER,
    season_start DATE,
    season_end DATE,
    goal_for INTEGER,
    goal_against INTEGER,
    matches_played INTEGER NOT NULL,
    wins INTEGER NOT NULL,
    losses INTEGER NOT NULL,
    draws INTEGER NOT NULL,
    PRIMARY KEY (team_id, season_start, season_end),
    FOREIGN KEY (season_start, season_end) REFERENCES season(start_year,end_year),
    FOREIGN KEY (team_id) REFERENCES team(id)
);

CREATE TABLE player_season(
    player_id INTEGER,
    season_start DATE,
    season_end DATE,
    matches_played INTEGER,
    goals_scored INTEGER,
    goals_against INTEGER,
    FOREIGN KEY (season_start, season_end) REFERENCES season(start_year,end_year),
    PRIMARY KEY (player_id, season_start, season_end)
    );
