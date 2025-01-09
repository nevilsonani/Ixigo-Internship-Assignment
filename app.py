import os
import uuid
from datetime import datetime, timedelta

import flask
import httplib2
import requests
from flask import redirect, render_template, request, session, url_for
from googleapiclient.discovery import build  # Corrected import
from oauth2client import client
from rfc3339 import rfc3339

app = flask.Flask(__name__)
app.secret_key = str(uuid.uuid4())

# News API Key (Replace with your NewsAPI key)
NEWS_API_KEY = "your_news_api_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if "credentials" not in session:
        return redirect(url_for("oauth2callback"))

    credentials = client.OAuth2Credentials.from_json(session["credentials"])
    if credentials.access_token_expired:
        return redirect(url_for("oauth2callback"))

    news_articles = []
    if request.method == "POST":
        topic = request.form["topic"]
        news_articles = fetch_news(topic)

    return render_template("index.html", articles=news_articles)

def fetch_news(topic):
    """Fetch news articles related to a topic from the last two weeks."""
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&from={(datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d')}"
        f"&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    return []

@app.route("/oauth2callback")
def oauth2callback():
    flow = client.flow_from_clientsecrets(
        "client_secrets.json",
        scope="https://www.googleapis.com/auth/calendar",
        redirect_uri=url_for("oauth2callback", _external=True),
    )
    if "code" not in request.args:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)
    else:
        auth_code = request.args.get("code")
        credentials = flow.step2_exchange(auth_code)
        session["credentials"] = credentials.to_json()
        return redirect(url_for("index"))

@app.route("/add_event", methods=["POST"])
def add_event():
    """Add a selected news article as an event in Google Calendar."""
    if "credentials" not in session:
        return redirect(url_for("oauth2callback"))

    credentials = client.OAuth2Credentials.from_json(session["credentials"])
    if credentials.access_token_expired:
        return redirect(url_for("oauth2callback"))

    http_auth = credentials.authorize(httplib2.Http())
    service = build("calendar", "v3", http=http_auth)

    title = request.form["title"]
    description = request.form["description"]
    start_time = datetime.now() + timedelta(hours=1)
    end_time = start_time + timedelta(hours=1)

    event = {
        "summary": title,
        "description": description,
        "start": {"dateTime": rfc3339(start_time)},
        "end": {"dateTime": rfc3339(end_time)},
    }

    service.events().insert(calendarId="primary", body=event).execute()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
