from flask import request, jsonify
import time
import sys
import socket


class Routes():

    def __init__():
        super()

    @classmethod
    def root(cls):
        return jsonify({
            "timestamp": time.time(),
            "hostname": socket.gethostname(),
            "engine": sys.version,
            "visitor ip": request.remote_addr
        })

    @classmethod
    def healthcheck(cls):
        return jsonify({
            "healthcheck": True,
        })
