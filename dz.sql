CREATE TABLE IF NOT EXISTS Artist (
 id_artist SERIAL PRIMARY key,
 Artist_name VARCHAR(50) NOT NULL unique,
 id_genre INTEGER NOT NULL unique
);
CREATE TABLE IF NOT EXISTS Albums (
 id_album SERIAL PRIMARY key,
 Albums_name VARCHAR(100) NOT NULL,
 Albums_year VARCHAR(4) NOT NULL,
 id_artist INTEGER REFERENCES Artists(id_artist) NOT NULL
);
CREATE TABLE IF NOT EXISTS Tracks (
 id_track SERIAL PRIMARY key,
 Track_name VARCHAR(100) NOT NULL,
Track_time VARCHAR(10) NOT NULL,
 id_album INTEGER REFERENCES Albums(id_album) NOT NULL
);
CREATE TABLE IF NOT EXISTS Genres (
 id_genre SERIAL PRIMARY key,
 Genre_name VARCHAR(100) NOT NULL UNIQUE
);
ALTER TABLE Artists ADD CONSTRAINT FOREIGN KEY (id_genre) REFERENCES Genres(id_genre);