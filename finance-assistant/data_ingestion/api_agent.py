import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API_KEY from .env

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_stock_data(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("Time Series (Daily)", {})
