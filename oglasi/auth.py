from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        # uzimamo podatke iz forme
        username = request.form.get("username")
        lozinka = request.form.get("password")
        db = get_db()
        error = None
        print(username, lozinka)
        # proveravamo da li korisnik sa datim username-om postoji
        korisnik = db.execute(
            "SELECT * FROM korisnik WHERE username = ?", (username,)
        ).fetchone()

        if korisnik is None:
            error = "Netacan username i/ili lozinka."
        elif not korisnik['lozinka'] == lozinka:
            error = "Netacan username i/ili lozinka."

        if error is None:
            # ulogujemo korisnika
            session.clear()
            session["korisnik"] = korisnik
            return redirect(url_for("index"))

        flash(error)
    
    return render_template("auth/login.html")


    

@bp.route("/logout", methods=["GET"])
def logout():
    pass

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        lozinka = request.form.get('password')
        repeat = request.form.get('repeat')
        email = request.form.get('email')
        
        db = get_db()
        error = None

        if not username:
            error = 'Username je neophodan.'
        elif not lozinka:
            error = 'Lozinka je neophodna.'
        elif lozinka != repeat:
            error = 'Lozinke se ne poklapaju.'
        elif not email:
            error = 'Email je neophodan.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO korisnik (username, email, lozinka) VALUES (?, ?, ?)",
                    (username, email, lozinka),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Korisnik pod imenom {username} vec postoji."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')