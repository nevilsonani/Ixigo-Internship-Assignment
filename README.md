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

## Dependencies

This project requires the following Python libraries:

- **Flask**: A web framework for Python.
- **Requests**: For making HTTP requests to the NewsAPI.
- **Google API Client**: For interacting with the Google Calendar API.
- **OAuth2Client**: For handling OAuth authentication with Google services.
- **rfc3339**: For formatting date-time in RFC 3339 format for Google Calendar.

You can install all dependencies by running the following command:

```bash
pip install -r requirements.txt
