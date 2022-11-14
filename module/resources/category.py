from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from module.db import CATEGORIES

blp = Blueprint("category", __name__, description="Operations on category")

@blp.route("/category")
class CategoryList(MethodView):
    def get(self):
        return CATEGORIES

    def post(self):
        request_data = request.get_json()
        if (
            "id" not in request_data
            or "name" not in request_data
        ):
            abort(400, message="Need id and name for category")
        if request_data["id"] in [u["id"] for u in CATEGORIES]:
            abort(400, message="ID is taken")
        if request_data["name"] in [u["name"] for u in CATEGORIES]:
            abort(400, message="Name is taken")
        CATEGORIES.append(request_data)
        return request_data