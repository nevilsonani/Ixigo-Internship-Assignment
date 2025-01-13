# Ixigo-Internship-Assignment

# News Reader

This is a simple Flask application that allows users to:
1. Search for news articles based on a topic using NewsAPI.
2. Add selected news articles as events to their Google Calendar.

## Features
- Fetch news articles related to a given topic from the last two weeks.
- Add news articles as events to Google Calendar with OAuth2 authentication.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/nevilsonani/Ixigo-Internship-Assignment
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Create a config.py file with your News API key:

```bash
NEWS_API_KEY = 'your_news_api_key_here'
NEWS_API_URL = 'https://newsapi.org/v2/everything'
```

### 4. Get a NewsAPI Key:

- Go to NewsAPI, sign up, and obtain your API key.
- Replace your_news_api_key in the code with your API key.



<h2>Running the App</h2>

1. Run the Flask application:

```bash
 python app.py
```

2.  Open your browser and go to http://127.0.0.1:5000/

<h3>File Structure</h3>

# News Reader

A simple news reader application built using Python and Flask that fetches news articles based on a topic from the past two weeks using the News API.

## Folder Structure

```plaintext
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── config.py
├── requirements.txt
└── news_fetcher.py


## Usage

This project requires the following Python libraries:

1. Enter a topic in the input field and click "Search."
2. The application will fetch and display news articles related to the topic from the past two weeks.
