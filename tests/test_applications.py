
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

# Allow importing the project as a Python package
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from importlib import import_module

project_name = Path(__file__).resolve().parents[1].name
project = import_module(project_name)

create_app = project.create_app
routes = import_module(f"{project_name}.routes")


@pytest.fixture
def client(monkeypatch):
    # Use a test configuration, not the real PostgreSQL database
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")

    app = create_app()
    app.config["TESTING"] = True

    return app.test_client()


def test_get_applications(client, monkeypatch):
    # Simulate one job application
    example = SimpleNamespace(
        id=1,
        user_id=1,
        job_id=1,
        status="Applied"
    )

    class FakeApplication:
        query = SimpleNamespace(all=lambda: [example])

    monkeypatch.setattr(routes, "Application", FakeApplication)

    response = client.get("/applications")

    assert response.status_code == 200
    assert response.get_json() == [{
        "id": 1,
        "user_id": 1,
        "job_id": 1,
        "status": "Applied"
    }]


def test_update_nonexistent_application(client, monkeypatch):
    # Simulate an application that does not exist
    monkeypatch.setattr(
        routes.db.session, "get", lambda model, key: None
    )

    response = client.put(
        "/applications/999",
        json={"status": "Interview"}
    )

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "Application not found"
    }


def test_delete_nonexistent_application(client, monkeypatch):
    # Simulate an application that does not exist
    monkeypatch.setattr(
        routes.db.session, "get", lambda model, key: None
    )

    response = client.delete("/applications/999")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "Application not found"
    }

def test_get_applications_filter_by_status(client, monkeypatch):
    # Simulate two applications with different statuses
    applications = [
        SimpleNamespace(id=1, user_id=1, job_id=1, status="Applied"),
        SimpleNamespace(id=2, user_id=1, job_id=2, status="Interview"),
    ]

    class FakeQuery:
        def filter_by(self, **kwargs):
            assert kwargs == {"status": "Applied"}
            filtered = [
                app for app in applications
                if app.status == kwargs["status"]
            ]
            return SimpleNamespace(all=lambda: filtered)

    class FakeApplication:
        query = FakeQuery()

    monkeypatch.setattr(routes, "Application", FakeApplication)

    response = client.get("/applications?status=Applied")

    assert response.status_code == 200
    assert response.get_json() == [{
        "id": 1,
        "user_id": 1,
        "job_id": 1,
        "status": "Applied"
    }]
