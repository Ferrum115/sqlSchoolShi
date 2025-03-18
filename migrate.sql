create schema if not exists vr;

CREATE TABLE IF NOT EXISTS vr.cars (
  carID INT PRIMARY KEY,
  age INT NOT NULL,
  model TEXT NOT NULL,
  color TEXT NOT NULL,
  carType TEXT NOT NULL,
);

CREATE TABLE IF NOT EXISTS vr.accident (
  ID INT PRIMARY KEY,
  damaged TEXT[] NOT NULL,
  accidentDate DATE NOT NULL
  accidentCarID INT NOT NULL 
);