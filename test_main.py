from main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient
import json


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_certificate_of_deposit():
    response = client.get(
        "/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3&compounding_per_yr=1"
    )
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Certificate of Deposit (CD)",
        "Principal amount": 5000.0,
        "Interest Rate": 5.0,
        "Time in Years": 3,
        "Number of Compounding per Year": 1,
        "Certificate of Deposit (CD)": "5788.125000000001",
    }


# Compounding per year cannot be 0, as it is division by 0 error
def test_certificate_of_deposit_invalid_value():
    response = client.get(
        "/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3&compounding_per_yr=0"
    )
    assert response.json()["status_code"] == 500


# Years cannot be a float, as it is a type error
def test_certificate_of_deposit_invalid_type():
    response = client.get(
        "/certificate_of_deposit/?principal_amount=5000.0&interest_rate=5.0&yrs=3.5&compounding_per_yr=1"
    )
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "yrs"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            }
        ]
    }


def test_simple_interest_rate_main():
    response = client.get(
        "/simple_interest_rate/?amount_paid=5000&principle_amount=4500&months=12"
    )
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Simple Interest Rate",
        "Total amount paid": 5000,
        "Principle amount": 4500,
        "Interest Paid": 500,
        "Interest Rate": f"11.11111111111111%",
    }


def test_roi_main():
    response = client.get("/roi/?current_value_of_investment=100&cost_of_investment=80")
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Return on Investment",
        "Current Value of Investment": 100,
        "Cost of Investment": 80,
        "Return on Investment": f"25.0%",
    }


def test_calculate_enterprise_value_main():
    response = client.get(
        "/enterprise-value/?share_price=10.00&fully_diluted_shares_outstanding=100&total_debt=500.00&preferred_stock=500.00&non_controlling_interest=1000.00&cash_and_cash_equivalents=1000.00"
    )
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Enterprise Value",
        "Equity Value": 1000,
        "Total Debt": 500,
        "Preferred Stock": 500,
        "Non-Controlling Interest": 1000,
        "Cash & Cash Equivalents": 1000,
        "Enterprise Value": 2000,
    }


def test_calculate_treynor_ratio():
    response = client.get("/calculate_treynor_ratio/?returns=0.1,0.05,0.08,0.12,0.09&risk_free_rate=0.03")
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Treynor Ratio",
        "returns": [0.1, 0.05, 0.08, 0.12, 0.09],
        "risk_free_rate": 0.03,
        "treynor_ratio": 1.6
    }


def test_main():
    # Define test parameters
    order_type = "buy"
    symbol = "AAPL"
    stop_price = 150.0
    quantity = 10

    # Call the execute_stop_order function
    execute_stop_order(order_type, symbol, stop_price, quantity)

# Call the test_main function
test_main()
