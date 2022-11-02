from flask import Flask,jsonify

app_urls = Flask(__name__)

@app_urls.get('/hello')
def index():
    return "Hello world"

@app_urls.get("/")
def data():
    return jsonify({"message":"The new message"})