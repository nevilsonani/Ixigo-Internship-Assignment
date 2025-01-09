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

- Enable the Google Calendar API.
- Create OAuth 2.0 Credentials for a Web Application.
- Add http://localhost as the Authorized Redirect URI.
- Download the client_secrets.json file and place it in the root directory of the project.

### 4. Get a NewsAPI Key:

- Go to NewsAPI, sign up, and obtain your API key.
- Replace your_news_api_key in the code with your API key.

### 5. Set up your client_secrets.json with your Google OAuth credentials. Here’s an example of the file structure:

```bash
{
  "installed": {
    "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uris": ["http://localhost"]
  }
}
```
- Replace YOUR_CLIENT_ID, YOUR_PROJECT_ID, and YOUR_CLIENT_SECRET with your own credentials obtained from the Google Developer Console.

<h4>Running the App</h4>

1. Run the Flask application:

```bash
 python app.py
