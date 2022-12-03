from main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient
import json


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

client = TestClient(app)

def test_certificate_of_deposit():
    response = client.get("/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3&compounding_per_yr=1")
    assert response.status_code == 200

    assert response.json() == {"Tag":"Certificate of Deposit (CD)",
            "Principal amount":5000.0,
            "Interest Rate":5.0,
            "Time in Years":3,
            "Number of Compounding per Year":1,
            "Certificate of Deposit (CD)": "5788.125000000001"
    }