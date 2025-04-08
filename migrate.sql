create schema if not exists vr;

CREATE TABLE IF NOT EXISTS vr.cars (
  carID INT PRIMARY KEY,
  age INT NOT NULL,
  model TEXT NOT NULL,
  color TEXT NOT NULL,
  carType TEXT NOT NULL
);


create table if not exists vr.a2c(
  carid references cars.ID
  accidentid references accident.ID
)

CREATE TABLE IF NOT EXISTS vr.accident (
  ID INT PRIMARY KEY,
  damaged TEXT[] NOT NULL,
  accidentDate DATE NOT NULL
);

--Get Functions
CREATE FUNCTION getCar(id INT) 
RETURNS TABLE AS $$
  SELECT * FROM cars WHERE carID = id;
$$ LANGUAGE sql;

CREATE FUNCTION getByType(cType TEXT) 
RETURNS TABLE AS $$
  SELECT * FROM cars WHERE carType = cType;
$$ LANGUAGE sql;

CREATE FUNCTION getByColor(c TEXT) 
RETURNS TABLE AS $$
  SELECT * FROM cars WHERE color = c;
$$ LANGUAGE sql;

CREATE FUNCTION getByModel(mdl TEXT) 
RETURNS TABLE AS $$
  SELECT * FROM cars WHERE model = mdl;
$$ LANGUAGE sql;

CREATE FUNCTION getByAge(minimum INT, maximum INT) 
RETURNS TABLE AS $$
  SELECT * FROM cars WHERE age BETWEEN minimum AND maximum;
$$ LANGUAGE sql;


-- Add Functions
CREATE FUNCTION addCar(id INT, ag INT, mdl TEXT, clr TEXT, typ TEXT) 
RETURNS VOID AS $$
  INSERT INTO cars (carID, age, model, color, carType) VALUES (id, ag, mdl, clr, typ);
$$ LANGUAGE sql;

CREATE FUNCTION addAccident(id INT, damage TEXT[], day DATE) 
RETURNS VOID AS $$
  INSERT INTO accident (ID, damaged, accidentDate) VALUES (id, damage, day);
$$ LANGUAGE sql;

-- Modify Functions
CREATE FUNCTION updateColor(id INT, newClr TEXT) 
RETURNS VOID AS $$
  UPDATE cars SET color = newClr WHERE carID = id;
$$ LANGUAGE sql;

CREATE FUNCTION updateAge(id INT, newAge INT) 
RETURNS VOID AS $$
  UPDATE cars SET age = newAge WHERE carID = id;
$$ LANGUAGE sql;

CREATE FUNCTION addAccidentToCar(id INT, accidentId INT) 
RETURNS VOID AS $$
  insert into a2c (carid, accidentid) values (id, accidentId);
$$ LANGUAGE sql;

-- Delete Functions
CREATE FUNCTION deleteCar(id INT) 
RETURNS VOID AS $$
  DELETE FROM cars WHERE carID = id;
  delete from a2c where id = carid;
$$ LANGUAGE sql;

CREATE FUNCTION deleteCarByAge(minimum INT, maximum INT) 
RETURNS VOID AS $$
  DELETE FROM cars WHERE age BETWEEN minimum AND maximum;
  delete from a2c where (select cars.carID where cars.age between minimum and maximum) = carid;
$$ LANGUAGE sql;

CREATE FUNCTION deleteCarByType(typ TEXT) 
RETURNS VOID AS $$
  DELETE FROM cars WHERE carType = typ;
  delete from a2c where (select cars.carID where cars.carType = typ) = carid;
$$ LANGUAGE sql;

CREATE FUNCTION deleteCarByModel(mdl TEXT) 
RETURNS VOID AS $$
  DELETE FROM cars WHERE model = mdl;
  delete from a2c where (select cars.carID where cars.model = mdl) = carid;
$$ LANGUAGE sql;

CREATE FUNCTION deleteAccident(id INT) 
RETURNS VOID AS $$
  DELETE FROM accident WHERE ID = id;
  delete from  a2c where id = accidentid;
$$ LANGUAGE sql;"						
