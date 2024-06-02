from flask import (
    redirect,
    url_for,
    request,
    session,
    Blueprint,
    flash,
)
from database import db
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.post("/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = db.session.execute(
        text("SELECT * FROM users WHERE username = :username"), {"username": username}
    ).one()

    valid = False
    if user:
        valid = check_password_hash(user.password, password)

    if not valid:
        flash("Invalid username or password", "danger")
        return redirect(url_for("index.index"))

    session["uid"] = user.id
    session["username"] = username

    flash("Logged in successfully", "success")

    return redirect(url_for("index.index"))


@bp.post("/register")
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    password2 = request.form.get("password2")

    if not password == password2:
        flash("Passwords must match", "danger")
        return redirect(url_for("index.index"))

    user_exists = db.session.execute(
        text("SELECT EXISTS(SELECT * FROM users WHERE username = :username)"),
        {"username": username},
    ).scalar()

    if user_exists:
        flash("User already exists", "danger")
        return redirect(url_for("index.index"))

    password_hashed = generate_password_hash(password)

    uid = db.session.execute(
        text(
            "INSERT INTO users (username, password, admin, date_created) VALUES (:username, :password, :admin, :date)"
        ),
        {
            "username": username,
            "password": password_hashed,
            "admin": False,
            "date": datetime.now(),
        },
    ).lastrowid

    db.session.commit()

    session["uid"] = uid
    session["username"] = username

    flash("Your account has been created", "success")

    return redirect(url_for("index.index"))


@bp.post("/logout")
def logout():
    del session["uid"]
    del session["username"]

    flash("Logged out successfully", "success")
    return redirect(url_for("index.index"))
