from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in a file named main.py

client = TestClient(app)


def test_create_asset():
    data = {
        "asset_id": "A001",
        "asset_type": "Laptop",
        "asset_name": "Dell XPS 13",
        "purchase_date": "2023-01-01",
        "purchase_cost": 1200.00,
        "vendor": "Dell Inc.",
    }
    response = client.post("/assets", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Asset created successfully"}


def test_read_assets():
    response = client.get("/assets")
    assert response.status_code == 200
    assert response.json() != []


def test_read_asset():
    asset_id = "A001"
    response = client.get(f"/assets/{asset_id}")

    response = client.get(f"/assets/{asset_id}")
    assert response.status_code == 200
    asset = response.json()
    assert asset["asset_id"] == "A001"
    assert asset["asset_type"] == "Laptop"
    assert asset["asset_name"] == "Dell XPS 13"
    assert asset["purchase_date"] == "2023-01-01"
    assert asset["purchase_cost"] == 1200.00
    assert asset["vendor"] == "Dell Inc."
    assert asset["status"] == "Active"
