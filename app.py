from flask import Flask, request, jsonify
from datetime import datetime
from service import TimesService, Schema
import json
app = Flask(__name__)
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return(f"Hello, the current system time is {datetime.now()}")

@app.route("/times", methods=["GET"])
def list_times():
    return jsonify(TimesService().list())

@app.route("/times", methods=["POST"])
def create_timer():
    return jsonify(TimesService().create(request.get_json()))

@app.route("/times/close", methods=["POST"])
def close_timer():
    return jsonify(TimesService().closeTimer(request.get_json()))

@app.route("/times/<item_id>", methods=["DELETE"])
def delete_timer(item_id):
    return jsonify(TimesService().delete(item_id))

if __name__ == "__main__":
    app.run(host='0.0.0.0')