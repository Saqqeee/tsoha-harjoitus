from datetime import datetime

from flask import render_template, Blueprint, redirect, url_for, request
from sqlalchemy.sql import text
from database import db

bp = Blueprint("categories", __name__, url_prefix="/category")


@bp.route("/")
def index():
    return redirect(url_for("index.index"))


@bp.route("/<int:category_id>")
def category(category_id):
    thread_list = []

    threads = db.session.execute(
        text(
            "SELECT id, title, last_active,"
            "(SELECT username FROM users WHERE id=threads.user_id)"
            "FROM threads WHERE cat_id = :cat_id ORDER BY last_active DESC"
        ),
        {"cat_id": category_id},
    ).all()

    for thread in threads:
        t = {
            "id": thread.id,
            "title": thread.title,
            "user": thread.username,
            "last_active": thread.last_active,
        }

        thread_list.append(t)

    return render_template("category.html", threads=thread_list, cat_id=category_id)


@bp.post("/add")
def add():
    name = request.form.get("name")
    description = request.form.get("description")

    db.session.execute(
        text(
            "INSERT INTO categories (name, last_active, description)"
            "VALUES (:name, :last_active, :description)",
        ),
        {"name": name, "last_active": datetime.now(), "description": description},
    )

    db.session.commit()

    return redirect(url_for("index.index"))
