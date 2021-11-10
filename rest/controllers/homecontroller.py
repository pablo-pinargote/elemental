import datetime

from flask import Response, request

from rest.decorators import get, post
from http import HTTPStatus


class HomeController:

    @get('/')
    def health_check(self):
        return {
                   'Hi': 'stranger',
                   'welcome': 'to the sample API',
                   'I': 'am healthy :) !',
                   'theTime': datetime.datetime.utcnow()
               }, HTTPStatus.OK

    @post('/apples')
    def payload(self):
        return Response({
            'theApple': request.json
        }, status=HTTPStatus.OK)
