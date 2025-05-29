from data_ingestion.api_agent import get_stock_data

if __name__ == "__main__":
    data = get_stock_data("MSFT")  # or AAPL, TSM
    print("Latest Close:", list(data.items())[0])
