import json
from flask import (Flask, render_template,
                   url_for, request)


app = Flask(__name__)
param = {'username': "Анатольев Алёша",
         'title': "Домашняя страница",
         'number': 8}


@app.route("/")
@app.route("/index")
def index():
    # http://127.0.0.1:8080/index
    return render_template('index.html', **param)


@app.route("/odd_even")
def odd_even():
    # http://127.0.0.1:8080/odd_even
    return render_template('odd_even.html', **param)


@app.route("/news")
def news():
    # http://127.0.0.1:8080/news
    with open("files/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    param_news = param
    param_news['news'] = news_list
    return render_template('news.html', **param_news)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')