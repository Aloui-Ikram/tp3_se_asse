from tkinter import *
def maj(nouvelleValeur):
# nouvelle valeur en argument
  print(nouvelleValeur)

def plus():
  Valeur.set(str(int (Valeur.get ())+10))
  print(Valeur.get ())

def moins():
  Valeur.set(str(int(Valeur.get())-10))
  print (Valeur.get ())

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title("Scale widget")
Valeur = StringVar()
Valeur.set (58)
# Création d'un widget Scale
echelle = Scale(Mafenetre, from_=-100, to=100, resolution=10, orient=HORIZONTAL ,
length=300, width=20,label="Offset",tickinterval=20,variable=Valeur,command=maj)
echelle.pack(padx=10, pady=10)

# Création d'un widget Button (bouton +)
Button(Mafenetre, text="+", command=plus).pack(padx=10, pady=10)

# Création d'un widget Button (bouton -)
Button(Mafenetre, text="-", command=moins).pack(padx=10, pady=10)

Mafenetre, mainloop()