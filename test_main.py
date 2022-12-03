from main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient
import json
# app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

client = TestClient(app)

def test_simple_interest_rate_main():
    response = client.get("/simple_interest_rate/?amount_paid=5000&principle_amount=4500&months=12")
    assert response.status_code == 200

    assert response.json() == {"Tag":"Simple Interest Rate",
            "Total amount paid":5000,
            "Principle amount":4500,
            "Interest Paid":500,
            "Interest Rate":f"11.11111111111111%"
    }

def test_roi_main():
    response = client.get("/roi/?gain_from_investment=100&cost_of_investment=2")
    assert response.status_code == 200

    assert response.json() == {
            "Tag":"Return on Investment",
            "Gain from Investment":100,
            "Cost of Investment":2,
            "Return on Investment":f"49.0%"
    }


