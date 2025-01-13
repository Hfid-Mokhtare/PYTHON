import tkinter as tk
from tkinter import messagebox


def show_info():
    prenom = entry_prenom.get()
    nom = entry_nom.get()
    age = entry_age.get()
    sexe = var_sexe.get()
    
    message = f"Prénom: {prenom}\nNom: {nom}\nÂge: {age}\nSexe: {sexe}"
    messagebox.showinfo("Informations enregistrées", message)
    

app = tk.Tk()
app.title("Inscription")
app.geometry("400x300")

frame = tk.Frame(app, bd=5, relief="solid", padx=90, pady=20)
frame.pack(padx=10, pady=10)  


label = tk.Label(frame, text="Inscription", font=("Arial", 30, "bold"))
label.pack(pady=20)

label = tk.Label(frame, text="Prénom:", font=("Arial", 15, "bold"))
label.pack()
entry_prenom = tk.Entry(frame, width=20, font=("Arial", 15))
entry_prenom.pack(pady=(0, 20))

label = tk.Label(frame, text="Nom:", font=("Arial", 15, "bold"))
label.pack()
entry_nom = tk.Entry(frame, width=20, font=("Arial", 15))
entry_nom.pack(pady=(0, 20))

label = tk.Label(frame, text="Age:", font=("Arial", 15, "bold"))
label.pack()
entry_age = tk.Entry(frame, width=20, font=("Arial", 15))
entry_age.pack(pady=(0, 20))

label = tk.Label(frame, text="Sexe:", font=("Arial", 15, "bold"))
label.pack()
var_sexe = tk.StringVar(value="Homme")

radio1 = tk.Radiobutton(frame, text="Homme", value='Homme', variable=var_sexe, font=("Arial", 12))
radio2 = tk.Radiobutton(frame, text="Femme", value='Femme', variable=var_sexe,font=("Arial", 12))
radio1.pack()
radio2.pack(pady=(0, 20))

label = tk.Label(frame, text="Sport", font=("Arial", 15, "bold"))
label.pack()
check1 = tk.Checkbutton(frame, text="Football", font=("Arial", 12))
check2 = tk.Checkbutton(frame, text="Basketball", font=("Arial", 12))
check3 = tk.Checkbutton(frame, text="Volleyball", font=("Arial", 12))
check1.pack()
check2.pack()
check3.pack(pady=(0, 20))

tk.Button(frame, 
       text="Afficher Info", 
       font=("Arial", 14, "bold"),
       bg="#3a8df3", 
       fg="white",   
       activebackground="#3a8df3",  
       activeforeground="black",
       relief="solid",
       width=30,
       height=2,
       command=show_info).pack()

app.mainloop()
