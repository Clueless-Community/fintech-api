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

#Compounding per year cannot be 0, as it is division by 0 error
def test_certificate_of_deposit_invalid_value():
    response = client.get("/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3&compounding_per_yr=0")
    assert response.json()["status_code"] == 500

#Years cannot be a float, as it is a type error
def test_certificate_of_deposit_invalid_type():
    response = client.get("/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3.5&compounding_per_yr=1")
    assert response.json() == {"detail": [{"loc": ["query", "yrs"],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"}]}