import uuid
from functools import wraps

from flask import request, make_response, jsonify
from src.api import app,db
from src.api.models import User, Type


def auth_required(f):
    @wraps(f)
    def decorator():

        return f(User.query.filter_by(id="1").first())
    return decorator
