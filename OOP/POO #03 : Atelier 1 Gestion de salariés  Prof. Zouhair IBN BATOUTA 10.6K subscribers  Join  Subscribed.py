class salarie:
    def __init__(self,matricule="",nom="",prenom="",salaire=0,tauxCS=0): 
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
        self.taux_charge_sociale=tauxCS
        
    def getter(self):
        return self
    
    def setter(self):
        self.nom="boulbane"
        
        
    def Afficher(self): 
        print(f"matricule : {self.matricule} , nom : {self.nom} , prenom : {self.prenom} ,salaire : {self.salaire} , taux_charge_sociale : {self.taux_charge_sociale}")

    def CalculeSalairNet(self):
        salairNait=self.salaire-(self.salaire * self.taux_charge_sociale)
        return salairNait
        print("le salaire net est : ",salairNait, " DH")

salarie1=salarie(input("enterer la matricule : "),input("enterer le nom : "), input("enterer le prenom : "),float(input("enterer le salaire : ")),float(input("enterer le taux : ")))
salarie1.Afficher()
print(f"le salaire net est : {salarie1.CalculeSalairNet()}")
        
