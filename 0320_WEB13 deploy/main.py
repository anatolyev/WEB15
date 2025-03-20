import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "Привет от приложения Flask"

def main():
    port = int(os.environ.get("PORT", 8080))
    app.run(port=port, host='0.0.0.0')

if __name__ == '__main__':
    main()
