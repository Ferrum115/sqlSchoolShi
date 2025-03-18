create schema if not exists vasyutinsky_ryabov;

CREATE TABLE IF NOT EXISTS vr.cars (
  carID INT PRIMARY KEY,
  age INT NOT NULL,
  model TEXT NOT NULL,
  color TEXT NOT NULL,
  carType TEXT NOT NULL,
  accidentID INT[]
);

CREATE TABLE IF NOT EXISTS vr.accident (
  ID INT PRIMARY KEY,
  damaged TEXT[] NOT NULL,
  accidentDate DATE NOT NULL
);