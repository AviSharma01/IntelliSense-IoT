CREATE TABLE temperature (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMP NOT NULL,
  temperature REAL NOT NULL,
  humidity REAL NOT NULL,
  category VARCHAR(50) NOT NULL
);
