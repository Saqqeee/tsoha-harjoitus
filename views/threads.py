from flask import render_template, Blueprint, redirect, url_for, request, session
from sqlalchemy.sql import text
from database import db
from datetime import datetime

bp = Blueprint("threads", __name__, url_prefix="/thread")


@bp.route("/")
def index():
    return redirect(url_for("index.index"))


@bp.route("/<int:thread_id>")
def thread(thread_id):
    post_list = []

    title = db.session.execute(
        text("SELECT title FROM threads WHERE id = :thread_id"),
        {"thread_id": thread_id},
    ).scalar()
    posts = db.session.execute(
        text(
            "SELECT id, text, date_created,"
            "(SELECT username FROM users WHERE id=posts.user_id)"
            "FROM posts WHERE thread_id = :thread_id ORDER BY id"
        ),
        {"thread_id": thread_id},
    ).all()

    for post in posts:
        p = {
            "id": post.id,
            "text": post.text,
            "date": post.date_created.strftime("%Y-%m-%d %H:%M:%S"),
            "user": post.username,
        }

        post_list.append(p)

    return render_template(
        "thread.html", title=title, posts=post_list, thread_id=thread_id
    )


@bp.post("/add")
def add():
    title = request.form.get("title")
    msg = request.form.get("message")
    cat = request.form.get("cat_id")
    uid = session["uid"]
    timestamp = datetime.now()

    thread_id = db.session.execute(
        text(
            "INSERT INTO threads (title, user_id, cat_id, last_active)"
            "VALUES (:title, :user_id, :cat_id, :last_active)"
            "RETURNING id"
        ),
        {"title": title, "user_id": uid, "cat_id": cat, "last_active": timestamp},
    ).scalar()

    db.session.execute(
        text(
            "INSERT INTO posts (user_id, thread_id, date_created, text)"
            "VALUES (:user_id, :thread_id, :date_created, :text)"
        ),
        {
            "user_id": uid,
            "thread_id": thread_id,
            "date_created": timestamp,
            "text": msg,
        },
    )
    db.session.commit()

    return redirect(url_for("threads.thread", thread_id=thread_id))


@bp.post("/comment")
def comment():
    msg = request.form.get("message")
    thread_id = request.form.get("thread_id")
    uid = session["uid"]
    timestamp = datetime.now()

    post_id = db.session.execute(
        text(
            "INSERT INTO posts (user_id, thread_id, date_created, text)"
            "VALUES (:user_id, :thread_id, :date_created, :text)"
            "RETURNING id"
        ),
        {
            "user_id": uid,
            "thread_id": thread_id,
            "date_created": timestamp,
            "text": msg,
        },
    ).scalar()

    db.session.commit()

    return redirect(url_for("threads.thread", thread_id=thread_id) + f"#{post_id}")
