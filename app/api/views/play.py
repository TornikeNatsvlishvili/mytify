from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
import pafy


class Play(MethodView):
    @jwt_required
    def get(self):
        if 'id' not in request.args:
            return jsonify('must supply id')
            
        