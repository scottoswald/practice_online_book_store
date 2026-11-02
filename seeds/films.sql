CREATE TABLE IF NOT EXISTS films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    genre TEXT,
    release_year INT,
    rating TEXT
);

TRUNCATE table films;

INSERT INTO films (title, genre, release_year, rating) VALUES ('Monsters Inc', 'Animated', 2001, 'G');
INSERT INTO films (title, genre, release_year, rating) VALUES ('The Shawshank Redemption', 'Drama', 1994, 'R');
INSERT INTO films (title, genre, release_year, rating) VALUES ('The Godfather', 'Gangster', 1972, 'R');
INSERT INTO films (title, genre, release_year, rating) VALUES ('The Dark Knight', 'Superhero', 2008, 'PG-13');