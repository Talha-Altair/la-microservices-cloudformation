from flask import Flask, render_template, jsonify
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

URL =  os.environ.get('BACKEND_URL')
PORT = os.environ.get('FRONTEND_PORT')

app = Flask(__name__)

@app.route('/ping')
def ping_pong():

    return jsonify({"ping":"Altair"})

@app.route('/')
def start():

    r = requests.get(URL)

    data = json.loads(r.content)

    return render_template('index.html', data=data["data"])

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port=PORT, debug=True)
