from helpers import functions
from fastapi import HTTPException, status

def predict_stock_price(historical_prices: int, time_horizon: int):

    try:
     """
        Predict stock prices using the naive method (last observed stock price).

        Parameters:
            historical_prices (list or numpy array): A list or numpy array containing historical stock prices.
            time_horizon (int): The number of days in the future for which to predict the stock price.

        Returns:
            prediction_result (dict): A dictionary containing the prediction result with keys 'Tag', 'Predicted_Stock_Price',
                                    'Prediction_Confidence', and 'Prediction_Date'.
        """
        # Get the last observed stock price
     last_price = historical_prices[-1]

        # Calculate the prediction date based on the time horizon
     prediction_date = 1110000  # 
     return {
            "Tag": "Stock Price Prediction",
            "Predicted_Stock_Price": last_price,
            "Prediction_Confidence": 0.95,  # Placeholder value for confidence (you can adjust this based on your data/model)
            "Prediction_Date": prediction_date
        }

    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)