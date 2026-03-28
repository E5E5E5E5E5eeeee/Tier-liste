import sqlite3

conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Classement")
cur.execute("DROP TABLE IF EXISTS Fictifs")
cur.execute("DROP TABLE IF EXISTS Roi")
cur.execute("DROP TABLE IF EXISTS Artistes")
cur.execute("DROP TABLE IF EXISTS Intellectuel")
cur.execute("DROP TABLE IF EXISTS Sportifs")

cur.execute("""CREATE TABLE IF NOT EXISTS Classement(prime INT PRIMARY KEY, categorie TEXT, surnom TEXT, titre TEXT, rang TEXT, pseudo TEXT, nom TEXT, FOREIGN KEY(surnom) REFERENCES Sportifs(surnom), FOREIGN KEY(titre) REFERENCES Fictifs(titre), FOREIGN KEY(rang) REFERENCES Roi(rang),FOREIGN KEY(pseudo) REFERENCES Artistes(pseudo), FOREIGN KEY(nom) REFERENCES Intellectuel(nom))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Sportifs(surnom TEXT PRIMARY KEY, prime INTEGER, image TEXT, sport TEXT, palmares TEXT, FOREIGN KEY(prime) REFERENCES Classement(prime))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Fictifs(titre TEXT PRIMARY KEY, prime INTEGER, image TEXT, univer TEXT, palmares TEXT, FOREIGN KEY(prime) REFERENCES Classement(prime))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Roi(rang TEXT  PRIMARY KEY, prime INTEGER, image TEXT, palmares TEXT, FOREIGN KEY(prime) REFERENCES Classement(prime))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Artistes(pseudo TEXT PRIMARY KEY, prime INTEGER, image TEXT, palmares TEXT, FOREIGN KEY(prime) REFERENCES Classement(prime))""")
cur.execute("""CREATE TABLE IF NOT EXISTS Intellectuel(nom TEXT PRIMARY KEY, prime INTEGER, image TEXT, palmares TEXT, FOREIGN KEY(prime) REFERENCES Classement(prime))""")

Sportifs = [

    ("King James", 95, "James.png", "Basket", "4x Champion NBA"),
    ("La Pulga", 103, "Messi.png", "Football", "8x Ballon d'Or"),
    ("Cr7", 102, "Ronaldo.png", "Football", "5x Ballon d'Or"),
    ("Iron Mike", 89, "Tyson.png", "Boxe", "Plus Jeune Champion Poids Lourds")
]

Fictifs = [
    ("Batman", 97, "Batman.png", "Gotham", "Batman > Superman"),
    ("Harry Potter", 77, "Harry.png", "Poudlard", "The boy who lived"),
    ("7th Hokage", 108, "Naruto.png", "Konoha", "L'enfant de la prophetie"),
    ("Sherlock Holmes", 88, "Sherlock.png", "London", "Le meilleure Detective"),
    ("James Bond", 87, "James_Bond.png", "MI6", "Meilleur Espion"),
    ("Superman", 109, "Superman.png", "Metropolis", "Man of Steel"),
    ("Spiderman", 110, "Spider.png", "New York", "Votre fidele serviteur"),
    ("Iron Man", 101, "Iron_Man.png", "New York", "Génie, PlayBoy, Philanthrope, Milliardaire"),
    ("Captain America", 55, "Captain.png", "Brooklyn", "Le Super-Soldat"),
    ("Thor", 86, "Thor.png", "Asgard", "Dieu du Tonnerre"),
    ("Wolverine", 60, "Wolverine.png", "Canada", "Mutant aux Griffes Acerees"),
    ("Black Panther", 100, "Black.png", "Wakanda", "Roi du Wakanda")
]

Roi = [
    ("Roi Soleil", 99, "Roi_Soleil.png", "Règne le Plus Long de l'Histoire de France"),
    ("Charlemagne", 70, "Roi_Soleil.png", "Fondateur de l'Empire Carolingien"),
    ("Henri VI", 69, "Henri.png", "Roi d'Angleterre et de France"),
    ("Alexandre le Grand", 68, "Alexandre.png", "Conquerant du Monde Connu"),
    ("Cyrus le Grand", 64, "Cyrus.png", "Fondateur de l'Empire Perse"),
    ("Ramsès II", 83, "Ramsès_II.png", "Plus Grand Pharaon d'Égypte"),
    ("Clovis", 62, "Clovis.png", "Unificateur des Francs"),
    ("Saladin", 65, "Saladin.png", "Roi de l'Égypte et de la Syrie"),
    ("Napoléon Bonaparte", 96, "Napoleon.png", "Empereur des Français")
]


Artistes = [
    ("Picasso", 67, "Picasso.png", "Fondateur du Cubisme"),
    ("Van Gogh", 80, "Vangogh.png", "Maitre Post-Impressionniste"),
    ("Da Vinci", 82, "Davinci.png", "Génie de la Renaissance"),
    ("Michelangelo", 98, "Michelangelo.png", "Maitre de la Chapelle Sixtine"),
    ("Monet", 71, "Monet.png", "Fondateur de l'Impressionnisme"),
    ("Dali", 56, "Dali.png", "Surrealiste par excellence"),
    ("Raphaël", 104, "Raphael.png", "Maitre de la Haute Renaissance"),
    ("Turner", 57, "Turner.png", "Peintre de paysages et maitre du romantisme")
]




Intellectuel = [
    ("Hawking", 81, "Hawking.png", "Theorie des Trous Noirs"),
    ("Currie", 85, "Currie.png", "Recherche sur la Radioactivite"),
    ("Freud", 106, "Freud.png", "Père de la Psychanalyse"),
    ("Darwin", 54, "Darwin.png", "Theorie de l'Evolution"),
    ("Descartes", 73, "Descartes.png", "Pere de la Philosophie Moderne"),
    ("Kant", 105, "Kant.png", "Philosophie Critique"),
    ("Nietzsche", 90, "Nietzche.png", "Philosophie du Surhomme")

]

Classement = [
    (95, "Sportif", "King James", None, None, None, None),
    (103, "Sportif", "La Pulga", None, None, None, None),
    (102, "Sportif", "Cr7", None, None, None, None),
    (89, "Sportif", "Iron Mike", None, None, None, None),
    (97, "Fictif", None, "Batman", None, None, None),
    (77, "Fictif", None, "Harry Potter", None, None, None),
    (108, "Fictif", None, "7th Hokage", None, None, None),
    (88, "Fictif", None, "Sherlock Holmes", None, None, None),
    (87, "Fictif", None, "James Bond", None, None, None),
    (109, "Fictif", None, "Superman", None, None, None),
    (110, "Fictif", None, "Spiderman", None, None, None),
    (101, "Fictif", None, "Iron Man", None, None, None),
    (55, "Fictif", None, "Captain America", None, None, None),
    (86, "Fictif", None, "Thor", None, None, None),
    (60, "Fictif", None, "Wolverine", None, None, None),
    (100, "Fictif", None, "Black Panther", None, None, None),
    (99, "Roi", None, None, "Roi Soleil", None, None),
    (70, "Roi", None, None, "Charlemagne", None, None),
    (68, "Roi", None, None, "Alexandre le Grand", None, None),
    (64, "Roi", None, None, "Cyrus le Grand", None, None),
    (83, "Roi", None, None, "Ramsès II", None, None),
    (62, "Roi", None, None, "Clovis", None, None),
    (65, "Roi", None, None, "Saladin", None, None),
    (96, "Roi", None, None, "Napoléon Bonaparte", None, None),
    (67, "Artiste", None, None, None, "Picasso", None),
    (80, "Artiste", None, None, None, "Van Gogh", None),
    (82, "Artiste", None, None, None, "Da Vinci", None),
    (98, "Artiste", None, None, None, "Michelangelo", None),
    (71, "Artiste", None, None, None, "Monet", None),
    (56, "Artiste", None, None, None, "Dali", None),
    (104, "Artiste", None, None, None, "Raphaël", None),
    (57, "Artiste", None, None, None, "Turner", None),
    (81, "Intellectuel", None, None, None, None, "Hawking"),
    (85, "Intellectuel", None, None, None, None, "Curie"),
    (106, "Intellectuel", None, None, None, None, "Freud"),
    (54, "Intellectuel", None, None, None, None, "Darwin"),
    (73, "Intellectuel", None, None, None, None, "Descartes"),
    (105, "Intellectuel", None, None, None, None, "Kant"),
    (90, "Intellectuel", None, None, None, None, "Nietzsche")

]



cur.executemany("INSERT INTO Sportifs VALUES (?, ?, ?, ?, ?)", Sportifs)
cur.executemany("INSERT INTO Fictifs VALUES (?, ?, ?, ?, ?)", Fictifs)
cur.executemany("INSERT INTO Roi VALUES (?, ?, ?, ?)", Roi)
cur.executemany("INSERT INTO Artistes VALUES (?, ?, ?, ?)", Artistes)
cur.executemany("INSERT INTO Intellectuel VALUES (?, ?, ?, ?)", Intellectuel)
cur.executemany("INSERT INTO Classement VALUES (?, ?, ?, ?, ?, ?, ?)", Classement)

conn.commit()
conn.close()

