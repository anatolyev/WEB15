from flask import Flask, url_for

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

@app.route("/image")
def image():
    # http://127.0.0.1:8080/image
    return f'''<img src="{url_for('static', filename='/images/image.jpg')}"
               alt="Это сова!">'''

@app.route("/sample_page")
def sample_page():
    # http://127.0.0.1:8080/sample_page
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" type="text/css" 
                    href="{url_for('static', filename='/css/style.css')}">
                    <title>Заголовок</title>
                </head>
                <body>
                <h1>Первая веб-страница!</h1>
                </body>
                </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')