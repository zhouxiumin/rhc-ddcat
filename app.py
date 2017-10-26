from flask import Flask, session
from flask_restful import Api

from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def default_route():
    return 'API reachable following the pattern /api/v1/*'


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    DEFAULT_PORT = 8080
    httpd = make_server('0.0.0.0', 8080, app)
    httpd.serve_forever()
