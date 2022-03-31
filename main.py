import sqlite3
from datetime import datetime

#alle entiteter slik de fremsto i 1.delinnlevering
bruker = """CREATE TABLE IF NOT EXISTS "bruker" (
	ID INTEGER PRIMARY KEY,
	fornavn	TEXT,
	etternavn	TEXT,
	epost	TEXT,
	passord	TEXT
);
"""

ferdigbrentKaffe = """CREATE TABLE IF NOT EXISTS "ferdigbrentKaffe" (
	kaffeID	INTEGER PRIMARY KEY,
	kilopris	INTEGER,
	beskrivelse	TEXT,
	navn	TEXT,
	brenningsdato	INTEGER,
	brenningsgrad	TEXT,
	partiID	INTEGER,
	brenneriID	INTEGER,
	FOREIGN KEY("partiID") REFERENCES "kaffeparti"("partiID"),
	FOREIGN KEY("brenneriID") REFERENCES "kaffebrenneri"("brenneriID")
);
"""

foredlingsmetode="""CREATE TABLE IF NOT EXISTS "foredlingsmetode" (
	FMetodeID	INTEGER PRIMARY KEY ,
	navn TEXT,
	beskrivelse TEXT
);
"""

gaard = """CREATE TABLE IF NOT EXISTS "gaard" (
	gaardID	INTEGER PRIMARY KEY,
	region	TEXT,
	gaardNavn	TEXT,
	landsID integer,
	moh	INTEGER,
	FOREIGN KEY("landsID") REFERENCES "land"("landsID")
);
"""


land = """CREATE TABLE IF NOT EXISTS "land" (
    landsID INTEGER PRIMARY KEY,
	landsnavn	TEXT NOT NULL
);
"""

kaffebonne = """CREATE TABLE IF NOT EXISTS "kaffebonne" (
	bonneID	INTEGER PRIMARY KEY,
	art	TEXT
);
"""


kaffebrenneri = """CREATE TABLE IF NOT EXISTS "kaffebrenneri" (
	brenneriID	INTEGER PRIMARY KEY,
	navn	TEXT
);
"""

kaffeparti = """CREATE TABLE IF NOT EXISTS "kaffeparti" (
	partiID	INTEGER PRIMARY KEY,
	aarHostet	INTEGER,
	kilopris	INTEGER,
	gaardID	INTEGER,
	FMetodeID	INTEGER,
	FOREIGN KEY("FMetodeID") REFERENCES "foredlingsmetode"("FMetodeID"),
	FOREIGN KEY("gaardID") REFERENCES "gaard"("gaardID")
);
"""

kaffesmaking = """CREATE TABLE IF NOT EXISTS "kaffesmaking" (
	kaffesmakingID	INTEGER PRIMARY KEY,
	dato INTEGER ,
	sNotater	TEXT,
	poeng	INTEGER,
	brukerID	INTEGER,
	kaffeID	INTEGER,
	FOREIGN KEY("brukerID") REFERENCES "bruker"("ID") ON DELETE CASCADE, 
	FOREIGN KEY("kaffeID") REFERENCES "ferdigbrentKaffe"("kaffeID")
);
"""

def create_database():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    cursor.execute(bruker)
    cursor.execute(foredlingsmetode)
    cursor.execute(kaffebrenneri)
    cursor.execute(kaffebonne)
    cursor.execute(gaard)
    cursor.execute(kaffeparti)
    cursor.execute(land)
    cursor.execute(ferdigbrentKaffe)
    cursor.execute(kaffesmaking)

    con.commit()
    con.close()

    return print('Database opprettet!')

#etabler database
def delete_data():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    cursor.execute("DELETE FROM foredlingsmetode")
    cursor.execute("DELETE FROM kaffebrenneri")
    cursor.execute("DELETE FROM kaffebonne")
    cursor.execute("DELETE FROM gaard")
    cursor.execute("DELETE FROM kaffeparti")
    cursor.execute("DELETE FROM land")
    cursor.execute("DELETE FROM ferdigbrentKaffe")
    cursor.execute("DELETE FROM kaffesmaking")
    cursor.execute("DELETE FROM bruker")

    con.commit()
    con.close()

    return print('Data slettet')

def create_testdata():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    #testdata
    cursor.execute("INSERT INTO bruker(fornavn, etternavn, epost, passord) VALUES ('Erik','Wahlstrøm', 'erik@gmail.com', 'passord123')")
    cursor.execute("INSERT INTO bruker(fornavn, etternavn, epost, passord) VALUES ('Mina','Sjøvik', 'mina@gmail.com', 'passord234')")
    cursor.execute("INSERT INTO bruker(fornavn, etternavn, epost, passord) VALUES ('Vegard','Hatleli', 'vegard@gmail.com', 'passord345')")


    cursor.execute("INSERT INTO foredlingsmetode(navn, beskrivelse) VALUES ('Vasket','Vasket i 10 minutter')")
    cursor.execute("INSERT INTO foredlingsmetode(navn, beskrivelse) VALUES ('Bærtørket','Tørket i 2 måneder')")

    cursor.execute("INSERT INTO kaffebrenneri(navn) VALUES ('Trondheim Brenneri')")
    cursor.execute("INSERT INTO kaffebrenneri(navn) VALUES ('Oslo Brenneri')")

    cursor.execute("INSERT INTO kaffebonne(art) VALUES ('Coffea Arabica')")
    cursor.execute("INSERT INTO kaffebonne(art) VALUES ('Coffea Robusta')")

    cursor.execute("INSERT INTO gaard(region,gaardNavn,landsID, moh) VALUES ('Kigali', 'El gaard',1, 1567)")
    cursor.execute("INSERT INTO gaard(region,gaardNavn,landsID, moh) VALUES ('Pereira','Los pollos',2,1024)")

    cursor.execute("INSERT INTO kaffeparti(aarHostet, kilopris, gaardID, FMetodeID) VALUES (2020, 100, 1, 1)")
    cursor.execute("INSERT INTO kaffeparti(aarHostet, kilopris, gaardID, FMetodeID) VALUES (2021, 75, 1, 2)")

    cursor.execute("INSERT INTO land(landsnavn) VALUES ('Rwanda')")
    cursor.execute("INSERT INTO land(landsnavn) VALUES ('Coloumbia')")

    cursor.execute("INSERT INTO ferdigbrentKaffe(kilopris, beskrivelse, navn, brenningsdato, brenningsgrad, brenneriID, partiID) VALUES (20,'Rund smak','Friele',110121,'Lys', 1, 1)")
    cursor.execute("INSERT INTO ferdigbrentKaffe(kilopris, beskrivelse, navn, brenningsdato, brenningsgrad, brenneriID, partiID) VALUES (15,'Spiss smak','Kjellsberg',120120,'Mørk',2, 2)")

    #direkte til brukerhistorie 1
    cursor.execute("INSERT INTO kaffebrenneri(navn) VALUES ('Jacobsen og Svart')")
    cursor.execute("INSERT INTO land(landsnavn) VALUES ('El Salvador')")
    cursor.execute("INSERT INTO gaard(region,gaardNavn,landsID, moh) VALUES ('Santa Ana','Nombre De Dios',3,1500)")
    cursor.execute("INSERT INTO kaffeparti(aarHostet, kilopris, gaardID, FMetodeID) VALUES (2021, 8, 3, 2)")
    cursor.execute("INSERT INTO ferdigbrentKaffe(kilopris, beskrivelse, navn, brenningsdato, brenningsgrad, brenneriID, partiID) VALUES (600,'En velsmakende og kompleks kaffe for mørketiden','Vinterkaffe 2022',200122,'Lysbrent', 3, 1)")

    cursor.execute("INSERT INTO kaffesmaking(dato, sNotater,poeng, brukerID, kaffeID) VALUES (19032022,'Dette smakte veldig godt, floral munnfølelse',8,1,1)")
    cursor.execute("INSERT INTO kaffesmaking(dato, sNotater,poeng, brukerID, kaffeID) VALUES (19052022,'Dette likte jeg ikke, floral aroma',3,1,2)")
    cursor.execute("INSERT INTO kaffesmaking(dato, sNotater,poeng, brukerID, kaffeID) VALUES (19042022,'Aromaen er rund, godt!!',7,2,1)")

    con.commit()
    con.close()

    return print('Testdata opprettet!')

#BRUKERHISTORIE 1
def create_kaffesmaking(id):
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    dato = datetime.now()
    dato = int(dato.strftime('%d%m%Y'))

    print('-------------------------------------------------')
    print('Opprett kaffesmaking ved å fylle ut informasjonen')
    kaffenavn = int(input('Hvilken kaffe (ID) smakte du? '))
    bruker = id
    poeng = int(input('Hvor mange poeng ønsker du å gi kaffen? '))
    notat = input('Skriv smaksnotat her: ')

    sql = "INSERT INTO kaffesmaking(dato, sNotater,poeng, brukerID, kaffeID) VALUES (?,?,?,?,?)"
    con.execute(sql, (dato,notat,poeng,bruker,kaffenavn))
    con.commit()
    con.close()

    return print('Gratulerer! Kaffesmaking er opprettet.')

#BRUKERHISTORIE 2
def most_unique_coffes_tasted():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    cursor.execute("SELECT bruker.fornavn, bruker.etternavn, COUNT(*) "
                   "from bruker LEFT OUTER JOIN kaffesmaking "
                   "ON bruker.ID = kaffesmaking.brukerID GROUP BY bruker.id")
    verdi = cursor.fetchall()
    print('Flest unike kaffesmakinger (synkende rekkefølge): ')
    print('--------------------------------------------------')
    print('Fornavn | Etternavn | Antall smakinger')
    for element in verdi:
        print(element)

    cursor.close()

#BRUKERHISTORIE 3
def highscore_per_price():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    cursor.execute("SELECT ferdigbrentKaffe.navn, ferdigbrentKaffe.kilopris, AVG(kaffesmaking.poeng) as score, kaffebrenneri.navn "
                   "FROM (kaffesmaking JOIN ferdigbrentKaffe ON kaffesmaking.kaffeID = ferdigbrentKaffe.kaffeID) "
                   "JOIN kaffebrenneri ON kaffebrenneri.brenneriID = ferdigbrentKaffe.brenneriID"
                   " GROUP BY ferdigbrentKaffe.kaffeID"
                   " ORDER BY score/ferdigbrentKaffe.kilopris DESC")
    verdi = cursor.fetchall()
    cursor.close()
    print('Kaffen som gir deg mest for pengene (score per pris)')
    print('----------------------------------------------------')
    print('Kaffenavn | Pris | Gj.poeng | Brenneri')

    for element in verdi:
        print(element)

#BRUKERHISTORIE 4
def floral_search():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()


    cursor.execute("SELECT kaffebrenneri.navn, ferdigbrentKaffe.navn "
                   "FROM (ferdigbrentKaffe JOIN kaffesmaking ON ferdigbrentKaffe.kaffeID = kaffesmaking.kaffeID) "
                   "JOIN kaffebrenneri ON ferdigbrentKaffe.brenneriID = kaffebrenneri.brenneriID"
                   " WHERE kaffesmaking.sNotater like '%floral%' OR ferdigbrentKaffe.beskrivelse like '%floral%'")
    verdi = cursor.fetchall()
    cursor.close()
    print('Alle søk med ordet floral')
    print('-------------------------')
    print('Brenneri | Kaffenavn')
    for element in verdi:
        print(element)

#BRUKERHISTORIE 5
def unwashed_from_RwaCol():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()


    cursor.execute("SELECT ferdigbrentKaffe.navn, kaffebrenneri.navn "
                   "FROM (foredlingsmetode JOIN kaffeparti ON foredlingsmetode.FMetodeID = kaffeparti.FMetodeID) "
                   "JOIN gaard ON gaard.gaardID = kaffeparti.gaardID "
                   "JOIN land ON gaard.landsID=land.landsID "
                   "JOIN ferdigbrentKaffe ON ferdigbrentKaffe.partiID = kaffeparti.partiID "
                   "JOIN kaffebrenneri ON ferdigbrentKaffe.brenneriID = kaffebrenneri.brenneriID"
                   " WHERE foredlingsmetode.navn!='Vasket' AND (land.landsnavn='Rwanda' OR land.landsnavn='Coloumbia')")
    verdi = cursor.fetchall()
    cursor.close()
    print('Uvaskede bønner fra Coloumbia og Rwanda')
    print('---------------------------------------')
    print('Kaffenavn | Brenneri')
    for element in verdi:
        print(element)

def delete_table():
    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()

    cursor.execute("DROP table kaffesmaking")

    con.commit()
    con.close()

def print_meny():
    print('MENY')
    print('1 - For å opprette ny kaffesmaking')
    print('2 - For liste over flest unike kaffesmakinger')
    print('3 - For hvilken kaffe som gir deg mest for pengene')
    print('4 - For alle kaffer med søkeordet floral')
    print('5 - For alle uvaskede kaffer fra Coloumbia og Rwanda')
    print('6 - For å avslutte')
    meny_letter = int(input('Skriv inn ønsket tall: '))
    return meny_letter

def create_user():
    fornavn = input('Fornavn: ')
    etternavn = input('Etternavn: ')
    epost= input('E-post: ')
    passord = input('Passord: ')

    con = sqlite3.connect("KaffeDB")
    cursor = con.cursor()
    sql = "INSERT INTO bruker(fornavn, etternavn, epost, passord) VALUES (?,?,?,?)"
    con.execute(sql,(fornavn, etternavn, epost, passord))
    con.commit()

    cursor.execute("SELECT * FROM bruker")
    verdi = cursor.fetchall()
    i = 0
    for element in verdi:
        i+=1
    con.close()
    return i


def main():
    user_login = 0
    print('Velkommen! Her kan du hente ut, samt opprette data tilknyttet Kaffedatabasen')
    print('----------------------------------------------------------------------------')
    bruker = input('Er du ny bruker (Y/N): ')
    if bruker == 'Y':
        user_login = create_user()
    if bruker == 'N':
        login_ID2 = int(input('Hva er bruker ID en din? '))
        user_login = login_ID2
    print(f'Du er logget inn med ID {user_login}')
    letter = input('Skriv inn M for meny, eller Q for avslutt: ')
    if letter == 'Q':
        return
    if letter == 'M':
        meny_letter = print_meny()
    bool_break = True

    while bool_break is True:
        if meny_letter == 1:
            create_kaffesmaking(user_login)
            back_to_meny = input('Trykk M for å gå tilbake til meny eller Q for å avlsutte: ')
            if back_to_meny == 'M':
                meny_letter = print_meny()
            if back_to_meny == 'Q':
                meny_letter = 6
        if meny_letter == 2:
            most_unique_coffes_tasted()
            back_to_meny = input('Trykk M for å gå tilbake til meny eller Q for å avlsutte: ')
            if back_to_meny == 'M':
                meny_letter = print_meny()
            if back_to_meny == 'Q':
                meny_letter = 6
        if meny_letter == 3:
            highscore_per_price()
            back_to_meny = input('Trykk M for å gå tilbake til meny eller Q for å avlsutte: ')
            if back_to_meny == 'M':
                meny_letter = print_meny()
            if back_to_meny == 'Q':
                meny_letter = 6
        if meny_letter == 4:
            floral_search()
            back_to_meny = input('Trykk M for å gå tilbake til meny eller Q for å avlsutte: ')
            if back_to_meny == 'M':
                meny_letter = print_meny()
            if back_to_meny == 'Q':
                meny_letter = 6
        if meny_letter == 5:
            unwashed_from_RwaCol()
            back_to_meny = input('Trykk M for å gå tilbake til meny eller Q for å avlsutte: ')
            if back_to_meny == 'M':
                meny_letter = print_meny()
            if back_to_meny == 'Q':
                meny_letter = 6
        if meny_letter == 6:
            bool_break = False


#main()
#Etabler database og testdata:
#create_database()
#create_testdata()

#støttefunksjoner:
#delete_data()
#delete_table()

#Brukerhistorier
#create_kaffesmaking()
#most_unique_coffes_tasted()
#highscore_per_price()
#floral_search()
#unwashed_from_RwaCol()
#create_user()

#Wow en odysse for smaksløkene: sitrusskall, melkesjokolade og aprikos.