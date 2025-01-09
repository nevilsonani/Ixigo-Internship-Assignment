# Ixigo-Internship-Assignment

# News Reader & Calendar Integration

This is a simple Flask application that allows users to:
1. Search for news articles based on a topic using NewsAPI.
2. Add selected news articles as events to their Google Calendar.

## Features
- Fetch news articles related to a given topic from the last two weeks.
- Add news articles as events to Google Calendar with OAuth2 authentication.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/news_calendar_app.git
cd news_calendar_app
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Create a new project in the Google Developer Console:

Enable the Google Calendar API.

Create OAuth 2.0 Credentials for a Web Application.

Add http://localhost as the Authorized Redirect URI.

Download the client_secrets.json file and place it in the root directory of the project.
