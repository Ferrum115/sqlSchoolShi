import psycopg2
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import json
#функции

app = FastAPI()

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
print("[connection established]")


@app.get("/")
async def root():
    return {"msg": "im awake and watching"}

#get func

@app.get("/get/cars/{id}")
async def getCar(id: int):
    r = cur.execute(f'SELECT * FROM vr.cars WHERE carID = {id};')
    return json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{cType}")
async def getCarByType(cType: str):
    r = cur.execute(f'SELECT * FROM vr.cars WHERE carType = {cType};')
    json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{c}")
async def getCarByColor(c: str):
    r = cur.execute(f'SELECT * FROM vr.cars WHERE color = {c};')
    json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{mdl}")
async def getCarByModel(mdl: str):
    r = cur.execute(f'SELECT * FROM vr.cars WHERE model = {mdl};')
    json.dumps(jsonable_encoder(r))

@app.get("/get/cars/{minimum}&{maximum}")
async def getCarByAge(minimum: int, maximum: int):
    r = cur.execute(f'SELECT * FROM vr.cars WHERE age BETWEEN {minimum} AND {maximum};')
    json.dumps(jsonable_encoder(r))

#add func

@app.post("/add/car/{id}&{ag}&{mdl}&{clr}&{typ}")
async def addCar(id: int, ag: int, mdl: str, clr: str, typ: str):
    cur.execute(f'INSERT INTO vr.cars (carID, age, model, color, carType) VALUES ({id}, {ag}, {mdl}, {clr}, {typ});')
    cur.commit()
    return 200

@app.post("/add/accident/{id}&{carid}&{damage}&{day}")
async def addAccident(id: int, carid: int, damage: str, day: int):
    cur.execute(f'INSERT INTO vr.accident (ID, damaged, accidentDate) VALUES ({id}, {damage}, {day});')
    cur.execute(f'insert into vr.a2c (carid, accidentid) values ({carid}, {id});')
    cur.commit()
    return 200

#update func

@app.put("/upd/car/{id}&{clr}")
async def updateColor(id: int, clr: str):
    cur.execute(f'UPDATE vr.cars SET color = {clr} WHERE carID = {id};')
    cur.commit()
    return 200
@app.put("/upd/car/{id}&{newAge}")
async def updateAge(id: int, newAge: int):
    cur.execute(f' UPDATE vr.cars SET age = {newAge} WHERE carID = {id};')
    cur.commit()
    return 200
@app.put("/upd/accident/{carid}&{accid}")
async def assingAccident(carid: int, accid: int):
    cur.execute(f'insert into vr.a2c (carid, accidentid) values ({carid}, {accid});')
    cur.commit()
    return 200

#delete func

@app.delete("/rem/car/{id}")
async def deleteCar(id: int):
    cur.execute(f'DELETE FROM cars WHERE carID = {id};')
    cur.execute(f'delete from a2c where {id} = carid;')
    cur.commit()
    return 200

@app.delete("/rem/car/{minimum}&{maximum}")
async def deleteCarByAge(minimum: int, maximum: int):
    cur.execute(f'DELETE FROM vr.cars WHERE age BETWEEN {minimum} AND {maximum};')
    cur.execute(f'delete from vr.a2c where (select cars.carID where cars.age between {minimum} and {maximum}) = carid;')
    cur.commit()
    return 200

@app.delete("/rem/car/{typ}")
async def deleteCarByType(typ: str):
    cur.execute(f'DELETE FROM vr.cars WHERE carType = {typ};')
    cur.execute(f'delete from vr.a2c where (select cars.carID where cars.carType = {typ}) = carid;')
    cur.commit()
    return 200

@app.delete("/rem/car/{mdl}")
async def deleteCarByModel(mdl: str):
    cur.execute(f'DELETE FROM vr.cars WHERE model = {mdl};')
    cur.execute(f'delete from vr.a2c where (select cars.carID where cars.model = {mdl}) = carid;')
    cur.commit()
    return 200

@app.delete("/rem/accident/{id}")
async def deleteAccident(id: int):
    cur.execute(f'DELETE FROM vr.accident WHERE ID = {id};')
    cur.execute(f'delete from vr.a2c where {id} = accidentid;')
    cur.commit()
    return 200

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9650)


# #сохраняем изменения
# cur.commit()

# #закрываем соединение
        
# cur.close()
# conn.close()