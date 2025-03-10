from flask import Flask, request, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lycey_key'

def main():
    app.run(port=8080, host='127.0.0.1')

@app.route("/")
@app.route("/index")
def index():
    # http://127.0.0.1:8080/index
    visit_count = int(request.cookies.get("visit_count", 0))
    if visit_count:
        res = make_response(f"Вы пришли на эту страницу {visit_count + 1} раз")
        res.set_cookie("visit_count", str(visit_count + 1), max_age=60*60*24*365*2)
    else:
        res = make_response(f"Вы пришли на эту страницу в первый раз")
        res.set_cookie("visit_count", "1", max_age=60*60*24*365*2)
    return res



if __name__ == '__main__':
    main()
