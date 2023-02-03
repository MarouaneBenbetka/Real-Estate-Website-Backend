import pytest
from src.api import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app



@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_get_annonces_route(client):
    response = client.get("/annonces/")
    print(response.json)
    assert response.status_code == 200
def test_delete_annonce(client):
    response = client.delete("/annonces/c8b2d3dc-9175-11ed-ac85-fc084ad74753",headers={'Authorization': 'Barer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2OTY0MjA2NC05MWFlLTExZWQtOTJhOC1mYzA4NGFkNzQ3NTMifQ.MIV_fT6AMDEXCv_IlcpD1wzhp2sEC5cPab7Szu0MViE'})
    response = client.get("/annonces/c8b2d3dc-9175-11ed-ac85-fc084ad74753")
    print(response.json)
    assert response.status_code == 400
def test_add_annonce(client):
    response = client.post("/annonces/",json={"typeId":1,"description":"test","surface":20,"wilaya":"Alger","price":20000,"category":"Vente","images":[],"commune":"cheraga","coordinates":{"latitude":10,"longitude":10}},headers={'Authorization': 'Barer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2OTY0MjA2NC05MWFlLTExZWQtOTJhOC1mYzA4NGFkNzQ3NTMifQ.MIV_fT6AMDEXCv_IlcpD1wzhp2sEC5cPab7Szu0MViE'})
    response = client.get(f"/annonces/{response.json['data']['id']}")
    assert response.status_code == 200