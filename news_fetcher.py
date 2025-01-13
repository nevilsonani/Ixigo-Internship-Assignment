import requests
from bs4 import BeautifulSoup
from config import NEWS_API_KEY, NEWS_API_URL

def fetch_news(query, from_date, to_date):
    params = {
        'q': query,
        'from': from_date,
        'to': to_date,
        'apiKey': NEWS_API_KEY
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        articles = data['articles']
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []
