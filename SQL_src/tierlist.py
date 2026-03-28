from tkinter import *
from PIL import ImageTk, Image
import sqlite3

fenetre = Tk()
fenetre.geometry("1000x750+150+20")
fenetre.configure(bg='#778899')

labels_img_tier = {"S": [], "A": [], "B": [], "C": [], "D": []}

couleurs_tiers = {
    "S": "#FF0000",
    "A": "#FF7F00",
    "B": "#FFFF00",
    "C": "#00FF00",
    "D": "#0000FF"
}

def charger_personnages():
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()

    liste_personnages = []

    requetes = [
        ("Sportif", "SELECT s.surnom, s.image, s.prime, s.palmares FROM Sportifs AS s"),
        ("Fictif", "SELECT f.titre, f.image, f.prime, f.palmares FROM Fictifs AS f"),
        ("Roi", "SELECT r.rang, r.image, r.prime, r.palmares FROM Roi AS r"),
        ("Artiste", "SELECT a.pseudo, a.image, a.prime, a.palmares FROM Artistes AS a"),
        ("Intellectuel", "SELECT i.nom, i.image, i.prime, i.palmares FROM Intellectuel AS i")
    ]

    for categorie, req in requetes:
        cur.execute(req)
        for nom, image, prime, palmares in cur.fetchall():
            liste_personnages.append((nom, image, prime, palmares))

    conn.close()
    return liste_personnages

personnages_liste = charger_personnages()
images_dict = {nom: ImageTk.PhotoImage(Image.open(image).resize((60, 60))) for nom, image, _, _ in personnages_liste}
classement = {nom: "Non classé" for nom, _, _, _ in personnages_liste}

def changer_classement(nom, nouv_tier, label_classement):
    global labels_img_tier, top

    classement[nom] = nouv_tier
    label_classement.config(text=f"Classement: {nouv_tier}")

    for tier, labels in labels_img_tier.items():
        for label in labels:
            if label["nom"] == nom:
                label["widget"].destroy()
                labels.remove(label)

    image = images_dict[nom]
    label_image = Label(top, image=image, bg=couleurs_tiers[nouv_tier], relief="solid", borderwidth=2)
    label_image.image = image

    x_pos = 250 + len(labels_img_tier[nouv_tier]) * 70
    y_pos = {"S": 20, "A": 100, "B": 180, "C": 260, "D": 340}[nouv_tier]
    label_image.place(x=x_pos, y=y_pos)

    labels_img_tier[nouv_tier].append({"nom": nom, "widget": label_image})

def ouvrir_fenetre_personnages(nom, prime, image_chem, palmares):
    top_perso = Toplevel(fenetre)
    top_perso.geometry("800x600")
    top_perso.config(bg="grey")
    top_perso.title(nom)

    Label(top_perso, text=f"Prime: {prime}", font=("Arial", 16), bg="grey").place(x=100, y=100)
    Label(top_perso, text=f"Palmarès: {palmares}", font=("Arial", 14), bg="grey").place(x=100, y=150)

    label_classement = Label(top_perso, text=f"Classement: {classement[nom]}", font=("Arial", 20), bg="grey")
    label_classement.place(x=100, y=300)

    for tier in ["S", "A", "B", "C", "D"]:
        Button(top_perso, text=tier, command=lambda t=tier: changer_classement(nom, t, label_classement)).place(x=100 + (50 * ["S", "A", "B", "C", "D"].index(tier)), y=400)

def toplevel():
    global top
    top = Toplevel(fenetre)
    top.geometry("1000x750+150+20")
    top.config(bg="black", relief="ridge", borderwidth=5)
    top.title("Classement")

    for tier, y_pos in {"S": 20, "A": 100, "B": 180, "C": 260, "D": 340}.items():
        Label(top, text=tier, font=("Arial", 50), bg=couleurs_tiers[tier], fg="white", height=1, width=4, relief="solid", borderwidth=3).place(x=50, y=y_pos)

    x_s, y_s = 60, 500
    x, y = x_s, y_s

    for nom, image_chem, prime, palmares in personnages_liste:
        image = images_dict[nom]
        Button(top, image=image, command=lambda n=nom, p=prime, ic=image_chem, pal=palmares: ouvrir_fenetre_personnages(n, p, ic, pal), borderwidth=2).place(x=x, y=y)
        x += 60
        if x >= 1000:
            x = x_s
            y += 65

Button(fenetre, text="Ouvrir la fenêtre pour créer un classement", command=toplevel, font=("Arial", 16), bg="white").pack(pady=30)

fenetre.mainloop()
