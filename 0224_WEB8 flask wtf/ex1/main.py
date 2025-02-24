from flask import (Flask, render_template,
                   url_for, request)


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    # http://127.0.0.1:8080/index
    param = {'username': "Анатольев Алёша",
             'title': "Домашняя страница"}

    return render_template('index.html', **param)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')