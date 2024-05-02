# Podešavanje lokalnog radnog okruženja

-   Upaliti powershell koristeći `WIN + R` i kucajući `powershell`
-   Navigirati na disk D: kucajući `D:`
-   Kreirati direktorijum sa vašim imenom i prezimenom kucajući
    `mkdir pera-peric`
-   Ući u dati repozitorijum kucajući `cd pera-peric`
-   Klonirati repozitorijum

```powershell
git clone <url-repozitorijuma>
```

-   Ući u repozitorijum kucajući `cd primer-pismenog`
-   Izvršiti sledeće komande

```powershell
pip install virtualenv
python -m virtualenv env
Set-ExecutionPolicy Unrestricted -Scope Process
env/Scripts/activate
pip install -r requirements.txt
flask --app oglasi run --debug
```

Trebalo bi da, nakon izvršavanja prethodnih komandi, se upali flask server na
portu `5000`.

## 1. Autentifikacija

Potrebno je definisati **Blueprint** nazvan `auth` koji sadrži rute:

-   `login`
-   `register`
-   `logout`

Definisati **Template** za:

-   `login`
-   `register`

Login template sadrži formu za unos username-a i password-a i podatke šalje
preko forme na odgovarajuću rutu. Nakon uspešnog login-a, uputiti korisnika na
početnu stranicu. Nakon neuspešnog, flash-ovati greške.

Register template sadrži formu za unos username-a, password-a i ponovljene
šifre, i podatke šalje preko forme na odgovarajuću rutu. Nakon uspešne
registracije, korisnika redirektovati na login template. Nakon neuspešne
registracije, flash-ovati greške.

Radi jednostavnosti, **ne heširati šifre**.

Koristeći dekorator iz flask-a, definisati funkciju koja učitava korisnikove
podatke iz sesije i smešta ih u globalni objekat.

Definisati dekorator koji brani pristup **View-ovima** ukoliko korisnik nije
ulogovan i redirektuje na login view.

## 2. Oglasi

### Blueprint

Napraviti `oglas.py` fajl koji definise **Blueprint** `oglas` sa prefiksom
`\oglas`. Registrovati dati **blueprint** u `__init__.py` fajlu.

### Kreiranje oglasa

Napraviti **view** i **template** za kreiranje novog oglasa. Link za kreiranje
novog oglasa treba biti dostupan samo ulogovanim korisnicima. Zabraniti pristup
putanji neulogovanim korisnicima koristeci kreirani dekorator. Forma koja kreira
oglas treba da ima inpute za:

-   Naslov
-   Opis
-   Kategoriju (select)
-   Cenu

### Prikaz oglasa

Napraviti **template** i **view** za prikaz svih oglasa. Raditi po uzoru na
`blog` **blueprint** iz flask tutorijala. Ukoliko je ulogovani korisnik vlasnik
oglasa, prikazati link za izmenu oglasa.

### Izmena oglasa

Napraviti **template** i **view** za izmenu postojecih oglasa. Dati link je
dostupan samo onom korisniku koji je kreirao oglas.

### Brisanje oglasa

Napraviti **view** za brisanje oglasa. Link ka ovoj ruti treba biti dostupan na
svakoj stranici za izmenu oglasa. Dozvoliti brisanje samo vlasnicima oglasa.
