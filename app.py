from flask import Flask, render_template, request
from datetime import datetime, timedelta
from news_fetcher import fetch_news

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    news = []
    if request.method == 'POST':
        query = request.form['query']
        to_date = datetime.now().strftime('%Y-%m-%d')
        from_date = (datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d')
        news = fetch_news(query, from_date, to_date)
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
