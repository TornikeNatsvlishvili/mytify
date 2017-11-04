from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token


class UserLogin(MethodView):
    @jwt_required
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

    def post(self):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

