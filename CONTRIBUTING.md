<h1 align=center> For the contributors 🫂 </h1>

### Haven't made your first-contribution yet? 😢
Do check our [First Contribution](https://github.com/Clueless-Community/first-contribution) repository, where we have provided the guidelines to set up Git and how to make a pull request !

# Project setup
## Fork and clone the repository
Copy the URL of the forked repository and clone it.
```bash
git clone https://github.com/<github_username>/fintech-api
```

## Change the directory
```bash
cd fintech-api
```

> Folder Structure
```
fintech-api
│
└───📂helpers
│   │   { Python functions for different calculations }
│
└───📂tasks
│   │   { Python functions for different tasks }
|
└───📂tests
│   |   { Python functions for different tests }
|
└───📂validators
│   │   { Pydantic Models for different validations }

📄.dockerfile
📄.gitignore
📄CODE_OF_CONDUCT.md
📄CONTRIBUTING.md
📄docker-compose.yml
📄Dockerfile
📄DOCUMENTATION.md
📄ENDPOINTS.md
📄LICENSE.md
📄main.py
📄README.md
📄requirements.txt
```


## Create a virtual environment
```bash
python -m venv env
```
## Activate the virtual environment
> For windows
```bash
env\Scripts\Activate.ps1
```
> For Linux
```bash
source env/bin/activate
```

## Install the dependencies
```powershell
pip install -r requirements.txt
```

## Run the FastAPI server
```powershell
uvicorn main:app --reload
```

## Run pytest
from root directory (FINTECH-API) where test_main.py is located
```powershell
pip install pytest # install pytest, only need to do once
pip install httpx
pytest #run the test
```

What to contribute?👀
Check the [project workflow](https://github.com/Clueless-Community/fintech-api/blob/main/CONTRIBUTING.md#project-workflow) section below.

Once you are done with the changes you wanted to add. Follow the steps to make the pull request.
## Create and checkout to the new branch.
```powershell
git checkout -b <branch_name>
```
## Add the changes
```
git add .
```

## Commit your change with a proper messagge
```
git commit -m "Enter your message here"
```

## Make the Pull Request
```
git push origin <branch_name>
```
---

# Project workflow
Briefly explaining, this project is an API providing endpoints that makes your financial calculation easy. This API can be easily integrated into websites, mobile applications, chrome extensions, etc. So how it works?

+ Once you run the server, and route to a path. For now, be it `/simple_interest_rate` (mentioned in **main.py**). You'll need to pass some query parameters.

+ As it is described, this endpoint returns the simple interest based on some input provided by the user.

+ Or you can route to the `/docs` path, where you can easily access and visualize the endpoints through a dashboard provided by swagger UI.

+ Here you can see, we are calling a function `simple_interest_rate()` that is defined inside `./helpers/functions.py`.
+ This function is responsible for making some calculations based on the parameter passed and returns the required value.

+ So, to add an endpoint, raise an issue regarding adding an endpoint. Once you are assigned, go through the [project setup ](https://github.com/Clueless-Community/fintech-api/blob/main/CONTRIBUTING.md#project-setup) and set up the project on the local machine.

+ Then create a function in `./helpers/functions.py`, passing the required parameters and returning the output as shown below
```python
# Function to Calculate Simple Interest Rate
def simple_interest_rate(amount_paid:float, principle_amount:float, months:int):
    term = months/12
    interest_paid = amount_paid-principle_amount
    rate = (interest_paid*100)/(principle_amount*term)
    return rate
```
+ Cross-validate your endpoint output from some online calculators available or even manually.

+ After completing with creating the function, create the request validation in `validators/request_validation.py` like this -

```python
class SimpleInterestRateRequest(BaseModel):
    amount_paid: float
    principle_amount: float
    months: int
```

+ Once the validation is done, create a task called `simple_interest.py` in `./tasks` and the task like this -

```python
def simple_interest_rate(amount_paid: float, principle_amount: float, months: int):
    try:
        rate = functions.simple_interest_rate(amount_paid, principle_amount, months)
        return {
            "Tag": "Simple Interest Rate",
            "Total amount paid": amount_paid,
            "Principle amount": principle_amount,
            "Interest Paid": amount_paid - principle_amount,
            "Interest Rate": f"{rate}%",
        }
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

+ Once the task is ready, create an endpoint in the `main.py` file following all the good practices of Fast API.

```python
@app.post(
    "/simple_interest_rate",
    tags=["simple_interest_rate"],
    description="Calculate simple interest rates",
)
def simple_interest_rate(request: SimpleInterestRateRequest):
    return simple_interest_rate_task(request.amount_paid, request.principle_amount, request.months)
```

+Also add your function in `ENDPOINTS.md`.
```
**POST** `/simple_interest_rate`

- Request body : `{
  "amount_paid": 20.23,
  "principle_amount": 30.9,
  "months": 5
}`
- Sample output

```py
{
  "Tag": "Simple Interest Rate",
  "Total amount paid": 20.23,
  "Principle amount": 30.9,
  "Interest Paid": -10.669999999999998,
  "Interest Rate": "-82.87378640776697%"
} ```
```
+Update the Docs
```
|---------------------------|----------------------------------------|---------------------------------------------------------|
| POST /simple_interest_rate | Calculate simple interest rates        | - `amount_paid` (float): The amount paid.               |
|                           |                                        | - `principle_amount` (float): The principle amount.     |
|                           |                                        | - `months` (int): The number of months.                 |
```
```
+ And that's it, you are now ready to make your pull request.

---

