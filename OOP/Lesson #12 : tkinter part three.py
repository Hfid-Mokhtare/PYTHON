import tkinter as tk
from tkinter import ttk # Theamed Tkinter Widgets

fenetre= tk.Tk()
fenetre.title("Tableau")
colonnes= ("Nom", "Age", "Ville")
tree= ttk.Treeview(fenetre, columns=colonnes, show="headings")
tree.pack(pady=20)
 # Definir les en-tetes de colonnes
tree.heading("Nom", text="Nom")
tree.heading("Age", text="Age")
tree.heading("Ville", text="Ville")

# Definir les dimensions des colonnes
tree.column("Nom", width=100, anchor="center")
tree.column("Age", width=100, anchor="center")
tree.column("Ville", width=100, anchor="center")

# Ajouter des donnees dans le tableau
donnes = {
("Amin", 25, "Tanger"),
("Mohamed", 25, "Tanger"),
("Ahmed", 25, "Tanger")

}

for element in donnes:
    tree.insert("","end",values=element)

# Lancement de la boucle principale
tree.mainloop()




