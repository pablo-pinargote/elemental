from http import HTTPStatus
from flask import Flask, Response
from werkzeug.exceptions import HTTPException
from rest import ResourcesMapper
from rest.controllers import HomeController

api = Flask(__name__)


@api.errorhandler(Exception)
def handle_exception(e):
    # Pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    # Non-HTTP exceptions are logged, but not passed through
    return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)


views = ResourcesMapper(api).register_actions(
    HomeController(),
)


if __name__ == '__main__':
    api.run('0.0.0.0', port=8200)
