import psycopg2
import uvicorn
import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient


# setup region

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
conn.autocommit = True


#мигрируем
cur.execute(open("migrate.sql", "r").read())
print("[connection established]")


# functions region

@app.get('/')
async def root():
    return {"msg": "im awake and watching"}

#get func

@app.get('/get/cars/byID/')
async def getCar(id: int):
    cur.execute(f'SELECT * FROM vasyutinsky_ryabov.cars WHERE carID = {id};')
    r = cur.fetchall()
    return JSONResponse(r)

@app.get('/get/cars/byType/')
async def getCarByType(cType: str):
    cur.execute(f'SELECT * FROM vasyutinsky_ryabov.cars WHERE carType = {cType};')
    r = cur.fetchall()
    return JSONResponse(r)

@app.get('/get/cars/byColor/')
async def getCarByColor(c: str):
    cur.execute(f'SELECT * FROM vasyutinsky_ryabov.cars WHERE color = {c};')
    r = cur.fetchall()
    return JSONResponse(r)

@app.get('/get/cars/byModel/')
async def getCarByModel(mdl: str):
    cur.execute(f'SELECT * FROM vasyutinsky_ryabov.cars WHERE model = {mdl};')
    r = cur.fetchall()
    return JSONResponse(r)

@app.get('/get/cars/byAge/')
async def getCarByAge(minimum: int, maximum: int):
    cur.execute(f'SELECT * FROM vasyutinsky_ryabov.cars WHERE age BETWEEN {minimum} AND {maximum};')
    r = cur.fetchall()
    return JSONResponse(r)

@app.get('/get/accidents/')
async def getAccidents():
    cur.execute(f'SELECT damaged, carid FROM vasyutinsky_ryabov.accident INNER JOIN vasyutinsky_ryabov.a2c ON accidentid = ID ORDER BY vasyutinsky_ryabov.accident.accidentDate ASC;')
    r = cur.fetchall()
    return JSONResponse(r)

#add func

@app.post('/add/car/')
async def addCar(id: int, ag: int, mdl: str, clr: str, typ: str):
    cur.execute(f'INSERT INTO vasyutinsky_ryabov.cars (carID, age, model, color, carType) VALUES ({id}, {ag}, {mdl}, {clr}, {typ});')
    conn.commit()
    return 200

@app.post('/add/accident/')
async def addAccident(id: int, carid: int, damage: str):
    cur.execute(f'INSERT INTO vasyutinsky_ryabov.accident (ID, damaged, accidentDate) VALUES ({id}, {damage}, \'{str(datetime.date.today())}\');')
    cur.execute(f'insert into vasyutinsky_ryabov.a2c (carid, accidentid) values ({carid}, {id});')
    conn.commit()
    return 200

#update func

@app.put('/upd/car/color/')
async def updateColor(id: int, clr: str):
    cur.execute(f'UPDATE vasyutinsky_ryabov.cars SET color = {clr} WHERE carID = {id};')
    conn.commit()
    return 200
@app.put('/upd/car/age/')
async def updateAge(id: int, newAge: int):
    cur.execute(f' UPDATE vasyutinsky_ryabov.cars SET age = {newAge} WHERE carID = {id};')
    conn.commit()
    return 200

#delete func

@app.delete('/rem/car/byID/')
async def deleteCar(id: int):
    cur.execute(f'delete from vasyutinsky_ryabov.a2c where {id} = carid;')
    cur.execute(f'DELETE FROM vasyutinsky_ryabov.cars WHERE carID = {id};')
    conn.commit()
    return 200

@app.delete('/rem/car/byAge/')
async def deleteCarByAge(minimum: int, maximum: int):
    cur.execute(f'delete from vasyutinsky_ryabov.a2c where (select cars.carID where cars.age between {minimum} and {maximum}) = carid;')
    cur.execute(f'DELETE FROM vasyutinsky_ryabov.cars WHERE age BETWEEN {minimum} AND {maximum};')
    conn.commit()
    return 200

@app.delete('/rem/car/byType/')
async def deleteCarByType(typ: str):
    cur.execute(f'delete from vasyutinsky_ryabov.a2c where (select cars.carID where cars.carType = {typ}) = carid;')
    cur.execute(f'DELETE FROM vasyutinsky_ryabov.cars WHERE carType = {typ};')
    conn.commit()
    return 200

@app.delete('/rem/car/byModel/')
async def deleteCarByModel(mdl: str):
    cur.execute(f'delete from vasyutinsky_ryabov.a2c where (select cars.carID where cars.model = {mdl}) = carid;')
    cur.execute(f'DELETE FROM vasyutinsky_ryabov.cars WHERE model = {mdl};')
    conn.commit()
    return 200

@app.delete('/rem/accident/')
async def deleteAccident(id: int):
    cur.execute(f'delete from vasyutinsky_ryabov.a2c where {id} = accidentid;')
    cur.execute(f'DELETE FROM vasyutinsky_ryabov.accident WHERE ID = {id};')
    conn.commit()
    return 200

# run

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9650)
