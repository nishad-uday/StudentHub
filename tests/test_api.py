
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app import database


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "test_students.db"

    monkeypatch.setattr(database, "DATABASE_PATH", test_db)

    with TestClient(app) as test_client:
        yield test_client


def test_crud_flow(client):
    payload = {
        "name": "Rahul Sharma",
        "date_of_birth": "2005-06-15",
        "email": "rahul@example.com",
        "phone": "9876543210",
        "course": "B.Tech CSE",
        "address": "Raipur, Chhattisgarh",
        "enrollment_date": "2024-08-01",
    }

    created = client.post("/students", json=payload)
    assert created.status_code == 201

    student_id = created.json()["student_id"]

    fetched = client.get(f"/students/{student_id}")
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "Rahul Sharma"

    updated_payload = {
        **payload,
        "course": "B.Tech AI & ML",
    }

    updated = client.put(
        f"/students/{student_id}",
        json=updated_payload,
    )
    assert updated.status_code == 200
    assert updated.json()["course"] == "B.Tech AI & ML"

    deleted = client.delete(f"/students/{student_id}")
    assert deleted.status_code == 204

    missing = client.get(f"/students/{student_id}")
    assert missing.status_code == 404


def test_invalid_student(client):
    response = client.post(
        "/students",
        json={
            "name": "R",
            "date_of_birth": "2005-06-15",
            "email": "not-an-email",
        },
    )

    assert response.status_code == 422


def test_missing_student(client):
    response = client.get("/students/999999")
    assert response.status_code == 404


def test_filter_and_pagination(client):
    payload = {
        "name": "Aman Baghel",
        "date_of_birth": "2004-05-10",
        "email": "aman@example.com",
        "course": "B.Tech CSE",
    }

    response = client.post("/students", json=payload)
    assert response.status_code == 201

    result = client.get(
        "/students",
        params={"course": "CSE", "limit": 10, "offset": 0},
    )

    assert result.status_code == 200
    assert len(result.json()) == 1
    assert result.json()[0]["name"] == "Aman Baghel"
