import psycopg2

#функции

def load(carId):
    cur.execute(f'SELECT carID={carId} from vr.cars;')
    return cur.fetchone()

def save(carId, carAge, carModel, carColor, carType):
    cur.execute(f'INSERT INTO vr.cars (carID, age, model, color, carType, accidentID) VALUES ({carId}, {carAge}, {carModel}, {carColor}, {carType})')
    print('car object saved')

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


#примеры функций
save(1, 10, 'porche911', 'blue', 'race')

load(1)

#сохраняем изменения
conn.commit()

#закрываем соединение            
cur.close()
conn.close()