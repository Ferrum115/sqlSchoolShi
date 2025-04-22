from fastapi.testclient import TestClient

from main import app

# testing region

client = TestClient(app)

def read_add_func_test():
    response = client.post('/add/cars/byID/?id=10&ag=10&mdl=sport&clr=blu&typ=yay')
    assert response.status_code == 200


def read_get_func_test():
    response = client.get("/get/cars/byID/?id=10")
    assert response.status_code == 200
    assert response.json() == {"carID": "10",
                               "age": "10",
                               "model": "sport",
                               "color": "blu",
                               "type": "yay"}

def read_put_func_test():
    response = client.put("/upd/car/color/?id=10&clr=red")
    assert response.status_code == 200

def read_del_func_test():
    response = client.delete("/rem/car/byID/")
    assert response.status_code == 200

# def read_add_func_test():
#     r = addCar(id=10, ag=10, mdl="sport", clr="blu", typ="yay")
#     if r['carID'] != '10':
#         print("car assignment failed")
#     if not r['carID']:
#         print("car assignment failed")
#     if r['age'] != '10':
#         print("car assignment failed")
#     if not r['age']:
#         print("car assignment failed")
#     if r['model'] != 'soprt':
#         print("car assignment failed")
#     if not r['model']:
#         print("car assignment failed")
#     if r['color'] != 'blu':
#         print("car assignment failed")
#     if not r['color']:
#         print("car assignment failed")
#     if r['carType'] != 'yay':
#         print("car assignment failed")
#     if not r['carType']:
#         print("car assignment failed")