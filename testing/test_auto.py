from fastapi.testclient import TestClient

from main import app

# testing region

client = TestClient(app)

def test_clear_table():
    response = client.delete("/clearall")
    assert response.status_code == 200

def test_add_func():
    response = client.post("/add/car/?id=10&ag=10&mdl='sport'&clr='blu'&typ='yay'")
    assert response.status_code == 200


def test_get_func():
    response = client.get("/get/cars/byID/?id=10")
    assert response.status_code == 200
    assert response.json() == [[10, 10, 'sport', 'blu', 'yay']]

def test_put_func():
    response = client.put("/upd/car/color/?id=10&clr='red'")
    assert response.status_code == 200

def test_del_func():
    response = client.delete("/rem/car/byID/?id=10")
    assert response.status_code == 200

def test_nonexistent_item():
    response = client.get("/get/cars/?id=848")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}