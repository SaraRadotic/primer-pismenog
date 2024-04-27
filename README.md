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
