CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN,
    date_created TIMESTAMP
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT,
    thread_id INT,
    date_created TIMESTAMP,
    text TEXT
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    user_id INT,
    cat_id INT,
    title TEXT,
    last_active TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    last_active TIMESTAMP
);
