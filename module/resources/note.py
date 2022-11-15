from flask import request

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from module.db import NOTES, USERS, CATEGORIES
from module.schemas import NoteSchema

blp = Blueprint("note", __name__, description="Operations on note")

@blp.route("/note")
class NoteList(MethodView):
    def get(self):
        user_id = request.args.get("user_id")
        category_id = request.args.get("category_id")
        if user_id and category_id:
            if int(user_id) not in [u["id"] for u in USERS]:
                abort(400, message="User fot found")
            if int(category_id) not in [u["id"] for u in CATEGORIES]:
                abort(400, message="Category fot found")
            notes = []
            for note in NOTES:
                if note["category_id"] == int(category_id) and note["user_id"] == int(user_id):
                    notes.append(note)
            return notes
        if user_id:
            if int(user_id) not in [u["id"] for u in USERS]:
                abort(400, message="User fot found")
            notes = []
            for note in NOTES:
                if note["user_id"] == int(user_id):
                    notes.append(note)
            return notes
        if category_id:
            if int(category_id) not in [u["id"] for u in CATEGORIES]:
                abort(400, message="Category fot found")
            notes = []
            for note in NOTES:
                if note["category_id"] == int(category_id):
                    notes.append(note)
            return notes
        return NOTES

    @blp.arguments(NoteSchema)
    def post(self, request_data):
        if request_data["id"] in [u["id"] for u in NOTES]:
            abort(400, message="ID is taken")
        if request_data["user_id"] not in [u["id"] for u in USERS]:
            abort(400, message="User fot found")
        if request_data["category_id"] not in [u["id"] for u in CATEGORIES]:
            abort(400, message="Category fot found")
        NOTES.append(request_data)
        return request_data
