from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "House Price Prediction API is running - CI/CD v2"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={
            "area_sqft": 1500,
            "bedrooms": 3,
            "bathrooms": 2,
            "parking": 2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_price_lakh" in data
    assert isinstance(data["predicted_price_lakh"], float)
    assert data["predicted_price_lakh"] > 0


def test_invalid_prediction_input():
    response = client.post(
        "/predict",
        json={
            "area_sqft": 1500,
            "bedrooms": 3
        }
    )

    assert response.status_code == 422
