import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Base de dados em memória para testes
SQLALCHEMY_TEST_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)
client = TestClient(app)

def test_health_check():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_create_task():
    r = client.post("/tasks/", json={"title": "Aprender DevOps", "priority": "high"})
    assert r.status_code == 201
    assert r.json()["title"] == "Aprender DevOps"
    assert r.json()["completed"] == False

def test_list_tasks():
    r = client.get("/tasks/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_update_task():
    create = client.post("/tasks/", json={"title": "Task para atualizar"})
    task_id = create.json()["id"]
    r = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert r.status_code == 200
    assert r.json()["completed"] == True

def test_delete_task():
    create = client.post("/tasks/", json={"title": "Task para apagar"})
    task_id = create.json()["id"]
    r = client.delete(f"/tasks/{task_id}")
    assert r.status_code == 204

def test_task_not_found():
    r = client.get("/tasks/99999")
    assert r.status_code == 404