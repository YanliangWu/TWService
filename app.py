import logging
from flask import Flask, jsonify
import time
import os

from flask import Flask, jsonify, request
import socket
import os
import atexit
from dao.DictDao import DictDao

from dao.EntryDao import EntryDao
from models.TwEntry import TWEntryRecord


app = Flask(__name__)

# Set up database connection

dao:EntryDao = DictDao()

@app.route("/")
def root():
    return jsonify(
        {
            "Message": "TW Service",
            "date": int(time.time()),
            "version": "1.0.0",
            "Kubernetes": "KUBERNETES_SERVICE_HOST" in os.environ,
        }
    )


@app.route("/v1/get_all_data")
def get_all_data():
    """
    Retrieve all the data 
    """
    app.logger.info(f"IP address: {request.remote_addr}, API: get_all_data")
    
    try:
        response = dao.get_all_rec()
        response = jsonify(response)
    except socket.gaierror:
        response = jsonify({"message": "Unable to resolve"}), 400
    return response


@app.route("/v1/insert_data", methods=["POST"])
def insert_data():
    """
    Insert a new record
    """
    data = request.get_json()
    if not data:
        return jsonify({"message": "Missing Payload"}), 400
    
    if not data.get("username"):
        return jsonify({"message": "Missing required field: username"}), 400

    if not data.get("description"):
        return jsonify({"message": "Missing required field: description"}), 400

    rec = TWEntryRecord.create_entry(data)
    dao.insert_new_rec(rec)
    return jsonify(rec.dict()), 200


@app.route("/v1/update_data", methods=["POST"])
def update_data():
    """
    Update an existed record by id, if id not found, then insert the record
    Basically, we need to find it first, then delete it, then update it.
    """
    data = request.get_json()
    target_id = data.get("id")

    if not data:
        return jsonify({"message": "Missing Payload"}), 400
    
    if not target_id:
        return jsonify({"message": "Missing required field: id"}), 400
    
    result = dao.update_rec(target_id, data)
    if not result.get("success"):
        return jsonify(result), 400
    
    return jsonify(result.get("payload")), 200


@app.route("/v1/delete_data", methods=["POST"])
def delete_data():
    """
    Delete existed record by id, if id not found, then return error message
    """
    data = request.get_json()
    id = data.get("id")
    if not data:
        return jsonify({"message": "Missing Payload"}), 400
    
    if not id:
        return jsonify({"message": "Missing required field: id"}), 400
    
    result = dao.delete_rec(id)
    return jsonify(result), 200


@atexit.register
def shutdown():
    print("Application Closed")


if __name__ == "__main__":
    atexit.register(shutdown)
    app.logger.setLevel(logging.INFO)
    app.run()
