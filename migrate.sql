create schema if not exists vasyutinsky_ryabov;

create table IF NOT EXISTS vasyutinsky_ryabov.car (
  carID INT PRIMARY KEY,
  age INT NOT NULL,
  model TEXT NOT NULL,
  color TEXT NOT NULL,
  carType TEXT NOT NULL,
  accidentID INT[]
)

create table IF NOT EXISTS vasyutinsky_ryabov.accident (
  ID INT PRIMARY KEY,
  damaged TEXT[] NOT NULL,
  accidentDate DATE NOT NULL
)