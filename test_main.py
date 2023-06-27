from main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient
import json


app = FastAPI()

  

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
    
# Endpoint to calculate the Net Income
def net_income():
    response = client.get("/net_income/", params={"revenue": 30000, "expenses": 25000})
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Net Income",
        "Revenue": 30000,
        "Expenses": 25000,
        "Net Income": 5000
    }

# Endpoint to calculate the break-even point
def break_even_point():
    response = client.get("/break_even_point/", params={"fixed_costs": 2500,"sales_price_per_unit": 2.95,"variable_price_per_unit":1.40 })
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Break-even Point",
        "Fixed Costs": 2500,
        "Sales Price Per Unit": 2.95,
        "Variable Price Per Unit": 1.40,
        "Break-even Point": f"1612.9032258064512"
    }

# Endpoint to calculate the Day Sales in Inventory Ratio   
def day_sales_in_inventory_ratio():
    response = client.get("/day_sales_in_inventory_ratio/", params={"avg_inventory":50000,"cost_of_goods_sold":200000,"no_of_days":365 })
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Day Sales in Inventory Ratio",
        "Average Inventory": 50000,
        "Cost of Goods Sold": 200000,
        "No of Days": 365,
        "Day Sales in Inventory Ratio": "91.25"
    }

# Endpoint to calculate the Cash Ratio   
def cash_ratio():
    response = client.get("/cash_ratio/", params={"cash":37.1,"cash_equivalents":26.8,"current_liabilities":123.5 })
    assert response.status_code == 200

    assert response.json() == {
        "Tag": "Cash Ratio",
        "Cash": 37.1,
        "Cash Equivalents": 26.8,
        "Current Liabilities": 123.5,
        "Cash Ratio": "0.52"
    }
