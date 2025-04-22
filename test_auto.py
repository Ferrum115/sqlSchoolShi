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
    response = client.delete("/rem/car/byID/?id=10")
    assert response.status_code == 200

def test_nonexistent_item():
    response = client.get("/get/cars/848")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}