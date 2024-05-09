DROP TABLE IF EXISTS oglas;
DROP TABLE IF EXISTS korisnik;
DROP TABLE IF EXISTS kategorija;

CREATE TABLE kategorija (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv TEXT NOT NULL
);

CREATE TABLE korisnik (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    lozinka TEXT NOT NULL
);

create TABLE oglas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naslov TEXT NOT NULL,
    opis TEXT NOT NULL,
    kategorija_id INTEGER NOT NULL,
    korisnik_id INTEGER NOT NULL,
    datum DATETIME DEFAULT CURRENT_TIMESTAMP,
    cena FLOAT NOT NULL,
    FOREIGN KEY (kategorija_id) REFERENCES kategorija(id),
    FOREIGN KEY (korisnik_id) REFERENCES korisnik(id)
);

-- Dodavanje kategorija
INSERT INTO kategorija (naziv) VALUES
('Automobili'),
('Nekretnine'),
('Elektronika'),
('Odeća i obuća'),
('Sport i rekreacija');

-- Dodavanje korisnika
INSERT INTO korisnik (username, email, lozinka) VALUES
('marko', 'marko@example.com', 'marko123'),
('ana', 'ana@example.com', 'ana456'),
('ivan', 'ivan@example.com', 'ivan789'),
('maja', 'maja@example.com', 'maja321'),
('stefan', 'stefan@example.com', 'stefan654');

-- Dodavanje oglasa
INSERT INTO oglas (naslov, opis, kategorija_id, korisnik_id, cena) VALUES
('Prodajem BMW', 'Odlično očuvan BMW serije 3, 2018. godište.', 1, 1, 15000.50),
('Stan u centru grada', 'Prostran stan sa tri sobe u centru grada.', 2, 2, 100000.00),
('iPhone 12 Pro Max', 'Novi iPhone 12 Pro Max sa 256GB prostora.', 3, 3, 1200.75),
('Jakna od eko kože', 'Crna jakna od eko kože, veličina M.', 4, 4, 50.00),
('Biciklistička kaciga', 'Crvena biciklistička kaciga, veličina L.', 5, 5, 20.99),
('Toyota Yaris', 'Toyota Yaris, 2017. godište, prešao 50,000 km.', 1, 2, 12000.00),
('Stan u novogradnji', 'Novi stan sa modernim dizajnom, 65m2.', 2, 3, 80000.00),
('Samsung 4K televizor', 'Samsung televizor dijagonale 55 inča, 4K rezolucija.', 3, 4, 899.99),
('Kožne čizme', 'Muške kožne čizme, braon boje, veličina 42.', 4, 5, 80.50),
('Fitnes sprava za trbušnjake', 'Fitnes sprava za trbušnjake, kao nova.', 5, 1, 150.00),
('Audi A4', 'Audi A4 Limousine, 2019. godište, dizel.', 1, 3, 25000.00),
('Vikendica na planini', 'Vikendica sa prelepim pogledom na planinu.', 2, 4, 150000.00),
('Sony PlayStation 5', 'Novi Sony PlayStation 5 sa dva kontrolera.', 3, 5, 499.99),
('Kratka haljina', 'Crvena kratka haljina, veličina S.', 4, 1, 30.00),
('Rolatni traka za trčanje', 'Rolatni traka za trčanje, odlično očuvana.', 5, 2, 200.00),
('Volkswagen Golf', 'Volkswagen Golf 7, 2016. godište, benzin.', 1, 4, 10000.00),
('Vikendica na jezeru', 'Vikendica idealna za odmor pored jezera.', 2, 5, 200000.00),
('LG Smart TV', 'LG Smart TV dijagonale 65 inča, Full HD rezolucija.', 3, 1, 799.99),
('Kožna jakna', 'Crna kožna jakna sa krznenim detaljima.', 4, 2, 120.00),
('Bicikl', 'Bicikl sa 21 brzinom, pogodan za vožnju po gradu.', 5, 3, 300.00),
('Prodajem stari laptop', 'Rabljeni laptop, dobro očuvan.', 3, 4, 150.00),
('Prodajem monitor', 'Monitor dijagonale 24 inča, Full HD rezolucija.', 3, 5, 99.99),
('Prodajem kuhinjski set', 'Kuhinjski set sa posuđem za 6 osoba.', 4, 1, 50.00),
('Prodajem biciklističku kacigu', 'Biciklistička kaciga, crna boja.', 5, 2, 25.00),
('Prodajem knjige', 'Komplet knjiga različitih žanrova.', 4, 3, 70.00);
