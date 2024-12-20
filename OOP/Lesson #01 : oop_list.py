from abc import ABC, abstractmethod

class institution (ABC):
    etudiants = []
    @abstractmethod
    def affichage():
        pass
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def remove():
        pass
    @abstractmethod
    def update():
        pass
    @abstractmethod
    def search():
        pass
    @abstractmethod
    def tri() :
        pass

class etudiant(institution) :
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
       
    def add(self):
        self.etudiants.append(self.nom)
        self.etudiants.append(self.prenom)
        self.etudiants.append(self.age)
        print("ajouter avec success !!")
       
    def remove(self):
        self.etudiants.remove(self.nom)
        self.etudiants.remove(self.prenom)
        self.etudiants.remove(self.age)
        print("supprimer avec success !!")
       
    def update(self) :
        self.etudiants[self.etudiants.index(self.nom)] = input("entrer le nouveeau nom : ")
        self.etudiants[self.etudiants.index(self.prenom)] = input("entrer le nouveau prenom : ")
        self.etudiants[self.etudiants.index(self.age)] = input("entrer le nouveau age : ")
        print("mise a jour avec success !!")
       
   
    def search(self):
        for i in range (0, len(self.etudiants),3) :
            if self.etudiants[i] == self.nom and self.etudiants[i+1] == self.prenom and self.etudiants[i+2] == self.age :
                print(f"{self.etudiants[i]}{self.etudiants[i+1]} est trouver avec succes ")
                break
            elif (i==len(self.etudiants)) :
                break

        
    def affichage(self):
        for i in range(0, len(self.etudiants), 3):
            print(self.etudiants[i], self.etudiants[i+1], self.etudiants[i+2])
   
    def tri(self) :
        self.etudiants.sort()
        print("Liste des etudiants triee par ordre alphabetique : ")

def menu () :
    while True :
        print("\n1. Ajouter un etudiant")
        print("2. Supprimer un etudiant")
        print("3. Modifier un etudiant")
        print("4. Rechercher un etudiant")
        print("5. Afficher la liste des etudiants")
        print("6. Trier la liste des etudiants")
        print("7. Quitter")
        
        choix = int(input("Votre choix : "))
        
        if choix == 1 :
            eleve = etudiant(input("Nom : "), input("Prenom : "), input("Age : "))
            eleve.add()
        elif choix == 2 :
            eleve = etudiant(input("Nom : "), input("Prenom : "), input("Age : "))
            eleve.remove()
        elif choix == 3 :
            eleve = etudiant(input("Nom : "), input("Prenom : "), input("Age : "))
            eleve.update()
        elif choix == 4 :
            eleve = etudiant(input("Nom : "), input("Prenom : "), input("Age : "))
            eleve.search()
        elif choix == 5 :
            eleve.affichage()
        elif choix == 6 :
            eleve.tri()
        elif choix == 7 :
            break
menu()
