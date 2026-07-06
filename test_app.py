import pytest 
from app import create_app
import store


@pytest.fixture
def client():
    store.reset()                     
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
    store.reset()                      

def test_create_item(client):
    response = client.post("/items", json={
        "name": "Notebook", "brand": "Moleskine", "price": 5.99
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Notebook"
 
 
def test_create_item_missing_name_fails(client):
    response = client.post("/items", json={"brand": "NoName"})
    assert response.status_code == 400
 
 
def test_get_items(client):
    client.post("/items", json={"name": "Pen"})
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
 
 
def test_get_item(client):
    created = client.post("/items", json={"name": "Pen"}).get_json()
    response = client.get(f"/items/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Pen"
 
 
def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
 
 
def test_update_item(client):
    created = client.post("/items", json={"name": "Pen", "quantity": 1}).get_json()
    response = client.patch(f"/items/{created['id']}", json={"price": 2.50})
    assert response.status_code == 200
    assert response.get_json()["price"] == 2.50
 
 
def test_delete_item(client):
    created = client.post("/items", json={"name": "Pen"}).get_json()
    response = client.delete(f"/items/{created['id']}")
    assert response.status_code == 200
 