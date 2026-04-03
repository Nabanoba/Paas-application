from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Railway!"

if __name__ == '__main__':
    app.run(debug=True)