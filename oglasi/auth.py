from flask import Blueprint, redirect, request, session, url_for

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET","POST"])
def login():
    username = request.form["username"]
    session["username"] = username
    return "OK"

@bp.route("/logout", methods=["GET"])
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@bp.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    session["username"] = username
    return "OK"