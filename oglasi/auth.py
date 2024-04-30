from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET","POST"])
def login():
    pass

@bp.route("/logout", methods=["GET"])
def logout():
    pass

@bp.route("/register", methods=["POST"])
def register():
    pass