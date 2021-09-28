#import statements
from main import app
from fastapi.testclient import TestClient


client_obj = TestClient(app)

okr_data = {
  "Objective": "Complete integrating python pytest program for api testing with Jenkins pipeline",
  "due_date": "1-October-2021",
  "completion_percentage": 100,
  "KeyResults": "Understand and implement different concepts in pytest, FASTAPI, Jenkins pipelines."
}

# Functions to test : Create, Read, Update and Delete OKR's.

def test_create_okr():
  response = client_obj.post("/okr/", json=okr_data)
  assert response.status_code == 200
  assert response.json() == okr_data

def test_get_all_okrs():
  response = client_obj.get("/okr/", json=okr_data)
  assert response.status_code == 200
  assert okr_data in response.json()

def test_get_okr():
  response = client_obj.get("/okr/0")
  assert response.status_code == 200
  assert response.json() == okr_data

def test_update_okr():
  update_okr_data = {
    "Objective": "Explore Openshift pipeline automation",
    "due_date": "31-October-2021",
    "completion_percentage": 100,
    "KeyResults": "Understand how Openshift pipelines work and hands on with automation."
  }
  response = client_obj.put("/okr/0", json= update_okr_data)
  assert response.status_code == 200
  assert response.json() == update_okr_data

def test_delete_okr():
  response = client_obj.delete("/okr/0")
  assert response.status_code == 200
  assert response.json() == {
    "Objective": "Explore Openshift pipeline automation",
    "due_date": "31-October-2021",
    "completion_percentage": 100,
    "KeyResults": "Understand how Openshift pipelines work and hands on with automation."
  }