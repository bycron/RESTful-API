#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/store', methods=['POST'])


def home():
    return "Hello, world!"

app.run(port=5000)