-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');

