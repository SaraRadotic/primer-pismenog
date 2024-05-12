from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from .db import get_db
bp = Blueprint("kategorije", __name__, url_prefix="/kategorije")

@bp.route("/", methods=["GET"])
def index():
    db = get_db()
    data = db.execute("SELECT naziv, COUNT(naziv) as broj FROM oglas join kategorija on oglas.kategorija_id = kategorija.id GROUP BY naziv").fetchall()
    print(data[0])
    return render_template("kategorije/index.html", data=data)