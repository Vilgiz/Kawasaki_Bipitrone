CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

INSERT INTO items (name, description) VALUES ('Item1', 'Description1');
