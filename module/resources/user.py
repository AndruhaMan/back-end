from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from module.db import USERS

blp = Blueprint("user", __name__, description="Operations on user")

@blp.route("/user")
class UsersList(MethodView):
    def get(self):
        return USERS

    def post(self):
        request_data = request.get_json()
        if (
            "id" not in request_data
            or "name" not in request_data
        ):
            abort(400, message="Need name for user")
        if request_data["id"] in [u["id"] for u in USERS]:
            abort(400, message="ID is taken")
        if request_data["name"] in [u["name"] for u in USERS]:
            abort(400, message="Name is taken")
        USERS.append(request_data)
        return request_data