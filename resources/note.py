
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import NoteModel
from schemas import NoteSchema, NoteQuerySchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("note", __name__, description="Operations on note")


@blp.route("/note")
class NoteList(MethodView):
    @blp.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NoteSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("user_id")
        category_id = kwargs.get("category_id")
        if user_id and category_id:
            query = NoteModel.query.filter_by(user_id=user_id, category_id=category_id)
            return query
        if user_id:
            query = NoteModel.query.filter_by(user_id=user_id)
            return query
        if category_id:
            query = NoteModel.query.filter_by(category_id=category_id)
            return query
        return NoteModel.query.all()

    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, request_data):
        note = NoteModel(**request_data)
        try:
            db.session.add(note)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Error when creating note")
        return note
