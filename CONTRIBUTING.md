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
fintect-api
│
└───📂helpers
│   │   { Python functions for different calculations }

📄.gitignore
📄CONTRIBUTING.md
📄main.py
📄README.md
📄requirements.txt
📄test_main.py
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

+ So, to add an endpoint, raise an issue regarding adding an endpoint. Once you are assigned, go through the [project setup ]() and set up the project on the local machine.

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

+ Once the function is ready, create an endpoint in the `main.py` file following all the good practices of Fast API.

```python
@app.get(
    "/simple_interest_rate",
    tags=["simple_interest_rate"],
    description="Calculate simple interest rates",
)
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

+Also add your funtion in `ENDPOINTS.md`.
```
**GET** `/simple_interest_rate`

- Required parameters : `amount_paid`, `principle_amount` and `months`
- Sample output

```py
{
    "Tag": "Simple Interest Rate",
    "Total amount paid": 5000.0,
    "Principle amount": 4500.0,
    "Interest Paid": 500.0,
    "Interest Rate": "11.11111111111111%"
}
```
```
+ And that's it, you are now ready to make your pull request.

---

