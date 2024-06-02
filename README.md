# Foorumi

## Aihe
Valitsin aiheeksi keskustelusovelluksen kurssimateriaalin esimerkeistä. Yhteenveto keskeisistä ominaisuuksista:

### Käyttäjät
Sovellukseen voi rekisteröityä, kirjautua, ja sieltä voi poistaa käyttäjätunnuksensa.
Jokaisella käyttäjällä on oma profiilisivu, jota voi mukauttaa (profiilikuva, lyhyt kuvaus yms.).
Käyttäjillä voi olla eri tason oikeuksia. Lähtökohtaisesti nämä tasot ovat ylläpitäjät ja rivikäyttäjät,
mutta suunnittelen tähän joustavamman ominaisuuden jos aika sallii.

### Viestit ja aihealueet
Käyttäjät voivat lähettää viestiketjuja niille tarkoitetuille aihealueille; ylläpitäjä voi mielensä mukaan järjestellä ja ryhmitellä näitä alueita.
Viestiketjuihin voi vastata ja muita viestiketjun viestejä voi lainata vastauksessa.
Viestin lähettäjä voi muokata tai poistaa viestinsä. Myös ylläpitäjillä on oikeus poistaa viestejä.
Viestejä voi myös hakea avainsanoilla.

## Vaihe
Sovellus on toistaiseksi vielä melko alkuvaiheillaan. Tällä hetkellä on mahdollista luoda käyttäjätunnus
ja kirjautua sisään/ulos sekä luoda aihealueita, aiheita ja kommentteja. Ylläpito-oikeuksia ei ole vielä
erikseen, vaan käyttäjätunnuksen omistaminen riittää kaikkiin toimintoihin. Tästä pohjasta on helppo lähteä
rakentamaan toimivaa sovellusta.

## Testaaminen
Asenna [PostgreSQL](https://www.postgresql.org/download/) ja luo sinne uusi tietokanta, jossa on
[schema.sql](schema.sql)-tiedoston osoittamat taulut.
Navigoi repositorion juurihakemistoon ja [luo virtuaaliympäristö](https://docs.python.org/3/library/venv.html) sekä
asenna sinne [tarvittavat moduulit](requirements.txt). Windowsin komentorivillä se käy näin:

```commandline
python3 -m venv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

Luo myös tiedosto .env tai aseta muulla tavalla seuraavat ympäristömuuttujat omaa järjestelmääsi vastaaviksi:
```properties
FLASK_SECRET_KEY=a1b2c3d4
FLASK_SQLALCHEMY_DATABASE_URI=postgresql://user:password@host:port/dbname
```

Tämän jälkeen sovelluksen pitäisi lähteä käyntiin yksinkertaisesti ajamalla `flask run`.