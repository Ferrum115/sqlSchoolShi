import psycopg2

hst = '79.174.88.238'
prt = 15221
name = 'school_db'
usr = 'school'
pswd = 'School1234*'
try:
    conn = psycopg2.connect(database=name, user=usr, password=pswd, host=hst, port=prt)
    with conn as cursor:
        cursor.execute(open("migrate.sql", "r").read())
except:
    print('bro ur database does weird shit')
finally:
    print(conn)