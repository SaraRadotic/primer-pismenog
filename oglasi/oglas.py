from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from .db import get_db
bp = Blueprint("oglas", __name__, url_prefix="/oglas")

@bp.route("/create", methods=["GET", "POST"])
def create():
    db = get_db()
    if request.method == "POST":
        print(request.form)
        naslov = request.form.get("naslov")
        opis = request.form.get("opis")
        kategorija = request.form.get("kategorija")
        cena = request.form.get("cena")
        uid = g.user["id"]
        
    
        db.execute(
            "INSERT INTO oglas (naslov, opis, kategorija_id, cena, korisnik_id) VALUES (?, ?, ?, ?, ?)",
            (naslov, opis, kategorija, cena, uid),
        )
        db.commit()
        return redirect(url_for("index"))
    kategorije = db.execute("SELECT * FROM kategorija").fetchall()
    return render_template("oglas/create.html", kategorije=kategorije)

@bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    db = get_db()
    if request.method == "POST":
        naslov = request.form.get("naslov")
        opis = request.form.get("opis")
        kategorija_id = request.form.get("kategorija")
        cena = request.form.get("cena")
        korsnik_id = g.user["id"]

        db.execute(
            "UPDATE oglas SET naslov = ?, opis = ?, kategorija_id = ?, cena = ?, korisnik_id = ? WHERE id = ?",
            (naslov, opis, kategorija_id, cena, korsnik_id, id),
        )
        db.commit()
    kategorije = db.execute("SELECT * FROM kategorija").fetchall()
    oglas = db.execute("SELECT * FROM oglas WHERE id = ?", (id,)).fetchone()
    return render_template("oglas/update.html", oglas=oglas, kategorije=kategorije)

@bp.route("/oglas/<int:id>", methods=["GET"])
def view(id):
    db = get_db()
    try:
        oglas = db.execute("SELECT * FROM oglas WHERE id = ?", (id,)).fetchone()
    except:
        flash("Oglas ne postoji")
        return redirect(url_for("oglas.index"))
    
    return render_template("oglas/view.html", oglas=oglas)

@bp.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    db = get_db()
    db.execute("DELETE FROM oglas WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("oglas.index"))

@bp.route("/kategorija/<int:id>", methods=["GET"])
def kategorija(id):
    db = get_db()
    oglasi = db.execute("SELECT * FROM oglas WHERE kategorija_id = ?", (id,)).fetchall()
    return render_template("index.html", oglasi=oglasi)