import tkinter as tk

def quitter():
    app1.quit()

def AddClient():
    global addclient_b
    addclient_b.config(text=" thanks for your click !")

app1 = tk.Tk()
app1.title("programme 1 :)") # ajouter le titre de la fenetere app
app1.geometry("300x300+510+50") # width x height + margin left + margin right

"""
Creation d'un composant graphique de type Label. Notez que l'on 
passe l'objet app comme premier parametre de construction pour indiquer qu'il appartient a la fenetre principale
"""
msg1 =tk.Label(app1, text="hello hello")
msg1.pack(side=tk.TOP) #Alignement a gauche

button=tk.Button(app1,text="exite", command=quitter)
button.pack(side="top")

addclient_b=tk.Button(app1,text="click me", command=AddClient)
addclient_b.pack(side="top")
#========================================================================================================================================

import tkinter as tk

def key_event(event):
    msg.config(text=f"Touche pressée : {event.char}")

def button_click(event):
    msg.config(text=f"Clic souris détecté : Bouton {event.num} à ({event.x}, {event.y})")

def button_release(event):
    msg.config(text=f"Bouton {event.num} relâché")

def double_click(event):
    msg.config(text=f"Double clic détecté : Bouton {event.num}")

def mouse_motion(event):
    msg.config(text=f"Déplacement de la souris à ({event.x}, {event.y})")

def mouse_enter(event):
    msg.config(text="La souris est entrée dans la zone !")

def mouse_leave(event):
    msg.config(text="La souris a quitté la zone !")
    
app2=tk.Tk()
app2.title("learn bind function ")

msg=tk.Label(app2,text="new message",font=("Arial",8))
msg.pack()

app2.bind("<Key>", key_event)  # Any key on the keyboard
msg.bind("<Button-1>", button_click)  # Left mouse button click
msg.bind("<Button-2>", button_click)  # Middle mouse button click
msg.bind("<Button-3>", button_click)  # Right mouse button click
msg.bind("<ButtonRelease-1>", button_release)  # Left mouse button release
msg.bind("<Double-Button-1>", double_click)  # Double left mouse button click
msg.bind("<Motion>", mouse_motion)  # Mouse movement
msg.bind("<Enter>", mouse_enter)  # Mouse enters the msg
msg.bind("<Leave>", mouse_leave)  # Mouse leaves the msg

#========================================================================================================================================

import tkinter as tk

app3=tk.Tk()
app3.title("form")

# to print a heading 
label=tk.Label(app3,text="this is a label", bg="blue", fg="white", font="Arial 20")
label.config(state=tk.NORMAL)
label.pack(pady=20)

# to reade input
label=tk.Label(app3,text="enter your name ")
label.pack()
entry=tk.Entry(app3)
entry.pack(pady=20)

# to do a checkbox
check1=tk.Checkbutton(app3, text="Option 1")
check2=tk.Checkbutton(app3, text="Option 2")
check1.pack()
check2.pack()

# to do a radio option
radio1=tk.Radiobutton(app3, text="Option A", value=1)
radio2=tk.Radiobutton(app3, text="Option B", value=2)
radio1.pack()
radio2.pack()

#========================================================================================================================================

import tkinter as tk

app4=tk.Tk()
app4.title("Liste")

liste=tk.Listbox(app4)
liste.pack()

liste.insert(0,"element 4")
liste.insert(1,"element 2")
liste.insert(2,"element 3")

liste.select_set(0)

label=tk.Label(app4,text="Selectionnez un element dans la liste")
label.pack()

taille=tk.Label(app4,text=f"Taille de la liste : {liste.size()}") # to get the size
taille.pack()




""" mainloop() affiche la fenetre et lance la boucle d'evenements."""
app1.mainloop()
app2.mainloop()
app3.mainloop()
app4.mainloop()

#========================================================================================================================================

import tkinter as tk
from tkinter import messagebox

def info():
    messagebox.showinfo("Information", "C'est une boite d'information")

def Avertissement():
    messagebox.showwarning("Avertissement", "C'est une boite d'Avertissement")

# boite d'error
def error():
    messagebox.showerror("Erreur","C'est une boite d'erreur")


# boite de confirmatoin OK/Annuler
def confirmer1():
    reponse= messagebox.askokcancel("Confirmation","Souhaitez-vous continuer ?")
    if reponse:
        print("user a choise de continuer")
    else: 
        print("user a annule l'action")

def confirmer2():
    reponse= messagebox.askyesno("Confirmation","Etes-vous sur?")
    if reponse:
        print("user a repondu Oui")
    else: 
        print("user a repondu Non")

window= tk.Tk()
window.title("Boites de message Tkinter")

btn_info= tk.Button(window, text="Afficher info", command=info)
btn_info.grid(row=0, column=0,padx=10,pady=5)

btn_info= tk.Button(window, text="Afficher Avertissement", command=Avertissement, bg="red", fg="white")
btn_info.grid(row=0, column=1,padx=10, pady=5)

btn_info= tk.Button(window, text="Afficher Erreur", command=error)
btn_info.grid(row=1, column=0,padx=10,pady=5)

btn_ok_annuler= tk.Button(window, text="Ok / Annuler",command=confirmer1)
btn_ok_annuler.grid(pady=5)

btn_ok_annuler= tk.Button(window, text="Oui / Non",command=confirmer2)
btn_ok_annuler.grid(row=1, column=1,padx=10,pady=5)

window.mainloop()


#========================================================================================================================================

import tkinter as tk
