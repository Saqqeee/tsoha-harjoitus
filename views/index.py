from flask import render_template, Blueprint
from sqlalchemy.sql import text
from database import db

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    cat_list = []

    categories = db.session.execute(
        text("SELECT * FROM categories ORDER BY last_active DESC")
    ).all()

    for category in categories:
        cat = {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "last_active": category.last_active,
        }

        cat_list.append(cat)

    return render_template("index.html", categories=cat_list)
