from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET","POST"])
def login():
    pass

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