

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 API de Delivery do Bruno está Online!</h1><p>Salvador, Bahia - 2026</p>"

if __name__ == '__main__':
    app.run()
