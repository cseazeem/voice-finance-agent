import requests
from bs4 import BeautifulSoup

def get_earning_surprises():
    url = "https://finance.yahoo.com/calendar/earnings"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table tbody tr")

    results = []
    for row in rows[:5]:  # first 5 entries
        cols = row.find_all("td")
        if len(cols) >= 6:
            results.append({
                "ticker": cols[0].text.strip(),
                "company": cols[1].text.strip(),
                "eps_estimate": cols[4].text.strip(),
                "eps_actual": cols[5].text.strip()
            })
    return results
