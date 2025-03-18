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
mg_command = ''
with open("migrate.sql") as f: #мигрируем
    mg_command = f.read()

with conn.cursor() as curse:
    for st in mg_command.split(";"):
        if st.strip():
            curse.execute(st.strip())

#примеры функций
save(1, 10, 'porche911', 'blue', 'race')

load(1)

#сохраняем изменения
conn.commit()

#закрываем соединение            
cur.close()
conn.close()