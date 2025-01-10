class entreprise: 
    def __init__(self,n,nbr):
        self.nom=n
        self.nombre_demployee=int(nbr)

    def afficher(self):
        print ("L'entreprise : ", self.nom,"\nNombre d'employee : ",self.nombre_demployee)

class salarie:
    # prendre un objet entre en parametre
    def __init__(self,matricule="",nom="",prenom="",salaire=0,tauxCS=0, entre=None): 
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
        self.taux_charge_sociale=tauxCS
        self.entre=entre
        
    def getter(self):
        return self
    
    def setter(self):
        self.nom="boulbane"
        
    # utillisation de la methode afficher de class l'entreprise dons la class salarie
    def Afficher(self): 
        print(f"matricule : {self.matricule} ,\nnom : {self.nom} ,\nprenom : {self.prenom}" 
              f" ,\nsalaire : {self.salaire} ,\ntaux_charge_sociale : {self.taux_charge_sociale}")
        self.entre.afficher()

    def CalculeSalairNet(self):
        salairNait=self.salaire-(self.salaire * self.taux_charge_sociale)
        return salairNait
       


E1=entreprise("ali",100)
E1.afficher()

salarie1=salarie("AAA","zeggaf","Mohamed Ali",1000,0.25,E1)
salarie1.Afficher()
print(f"le salaire net est : {salarie1.CalculeSalairNet()}")

salarie2=salarie("BBB","zeggaf","Yahya",2000,0.25,E1)
salarie2.Afficher()
print(f"le salaire net est : {salarie2.CalculeSalairNet()} ")
        
