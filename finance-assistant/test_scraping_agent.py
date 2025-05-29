from data_ingestion.scraping_agent import get_earning_surprises

if __name__ == "__main__":
    surprises = get_earning_surprises()
    for item in surprises:
        print(item)
