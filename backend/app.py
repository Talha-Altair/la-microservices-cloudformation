from flask import *
import json
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.environ.get('BACKEND_PORT')

app = Flask(__name__)

@app.route('/ping')
def ping_pong():

    return jsonify({"ping":"Altair"})

def get_json():

    json_file = open('data.json')
    json_data = json.load(json_file)

    return json_data

@app.route('/')
def start():

    data = get_json()

    return jsonify(data)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=PORT, debug=True)
