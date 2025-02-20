from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    # http://127.0.0.1:8080/index
    return "Привет, Яндекс!"

@app.route("/countdown")
def countdown():
    # http://127.0.0.1:8080/countdown
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append("Пуск!")
    return '<br>'.join(countdown_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')