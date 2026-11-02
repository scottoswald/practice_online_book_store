-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, password) VALUES ('Test One', 'Test One PW');
