import psycopg2
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import json
#функции

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "im awake and watching"}

#get func

@app.get("/get/cars/{id}")
def getCar(id: int):
    r = cur.execute(f'SELECT * FROM cars WHERE carID = {id};')
    return json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{cType}")
def getCarByType(cType: str):
    r = cur.execute(f'SELECT * FROM cars WHERE carType = {cType};')
    json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{c}")
def getCarByColor(c: str):
    r = cur.execute(f'SELECT * FROM cars WHERE color = {c};')
    json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{mdl}")
def getCarByModel(mdl: str):
    r = cur.execute(f'SELECT * FROM cars WHERE model = {mdl};')
    json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{minimum}&{maximum}")
def getCarByAge(minimum: int, maximum: int):
    r = cur.execute(f'SELECT * FROM cars WHERE age BETWEEN {minimum} AND {maximum};')
    json.dumps(jsonable_encoder(r))

#add func

@app.post("/add/car/{id}&{ag}&{mdl}&{clr}&{typ}")
def addCar(id: int, ag: int, mdl: str, clr: str, typ: str):
    cur.execute(f'INSERT INTO cars (carID, age, model, color, carType) VALUES (id, ag, mdl, clr, typ);')
    return 200

@app.post("/add/accident/{id}&{carid}&{damage}&{day}")
def addAccident(id: int, carid: int, damage: str, day: int):
    cur.execute(f'INSERT INTO accident (ID, damaged, accidentDate) VALUES ({id}, {damage}, {day});')
    cur.execute(f'insert into a2c (carid, accidentid) values ({carid}, {id});')
    return 200

#update func

@app.put("/upd/car/{id}&{clr}")
def updateColor(id: int, clr: str):
    cur.execute(f'UPDATE cars SET color = {clr} WHERE carID = {id};')
    return 200
@app.put("/upd/car/{id}&{newAge}")
def updateAge(id: int, newAge: int):
    cur.execute(f' UPDATE cars SET age = {newAge} WHERE carID = {id};')
    return 200
@app.put("/upd/accident/{carid}&{accid}")
def assingAccident(carid: int, accid: int):
    cur.execute(f'insert into a2c (carid, accidentid) values ({carid}, {accid});')
    return 200

#delete func

@app.delete("/rem/car/{id}")
def deleteCar(id: int):
    cur.execute(f'DELETE FROM cars WHERE carID = {id};')
    cur.execute(f'delete from a2c where {id} = carid;')
    return 200

@app.delete("/rem/car/{minimum}&{maximum}")
def deleteCarByAge(minimum: int, maximum: int):
    cur.execute(f'DELETE FROM cars WHERE age BETWEEN {minimum} AND {maximum};')
    cur.execute(f'delete from a2c where (select cars.carID where cars.age between {minimum} and {maximum}) = carid;')
    return 200

@app.delete("/rem/car/{typ}")
def deleteCarByType(typ: str):
    cur.execute(f'DELETE FROM cars WHERE carType = {typ};')
    cur.execute(f'delete from a2c where (select cars.carID where cars.carType = {typ}) = carid;')
    return 200

@app.delete("/rem/car/{mdl}")
def deleteCarByModel(mdl: str):
    cur.execute(f'DELETE FROM cars WHERE model = {mdl};')
    cur.execute(f'delete from a2c where (select cars.carID where cars.model = {mdl}) = carid;')
    return 200

@app.delete("/rem/accident/{id}")
def deleteAccident(id: int):
    cur.execute(f'DELETE FROM accident WHERE ID = {id};')
    cur.execute(f'delete from  a2c where {id} = accidentid;')
    return 200


#данные ДБшки
hst = '79.174.88.238'
prt = 15221
name = 'school_db'
usr = 'school'
pswd = 'School1234*'

#соединяемся
conn = psycopg2.connect(database=name, user=usr, password=pswd, host=hst, port=prt)
cur = conn.cursor()

#мигрируем
cur.execute(open("migrate.sql", "r").read())

#сохраняем изменения
conn.commit()

#закрываем соединение            
cur.close()
conn.close()