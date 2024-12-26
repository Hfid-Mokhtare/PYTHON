class entreprise: 
    def __init__(self,nom,nbr):
        self.nom=nom
        self.nombre_employee=nbr
    def Afficher(self):
        print("le nom de l'entreprise :",self.nom,"le nombre de employee :",
              self.nombre_employee)


class Salarie(entreprise):
    def __init__(self,matricule=None,nom=None,prenom=None,salaire=None
                 ,tauxCS=None):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.salaire:float=float(salaire)
        self.tauxCS:float=float(tauxCS)
        self.entr=e
    def afficher_info1(self):
        print("matricule :",self.matricule,"\nNom :",self.nom,
        "\nPrenom :",self.prenom,"\nSalaire :",self.salaire,
        "\nle nom de l'entreprise :",self.entr.nom,
        "\nle nom de l'entreprise :",self.entr.nombre_employee)

    def afficher_info2(self):
        print("matricule :",self.matricule,"\nNom :",self.nom,
        "\nPrenom :",self.prenom,"\nSalaire :",self.salaire)
        Afficher()


        
    def SalaireNet(self):
        return (self.salaire - (self.salaire*self.tauxCS))

E1=entreprise(input("enter your company name :"),
                int(input("Enter the number of employee in company :")))
E1.Afficher()

print ("-----------------------------")

S1=Salarie(1234,"zeggaf","mohamed ali",5000,0.25,E1)
S1.afficher_info1()
print("le salaire net est :",S1.SalaireNet(),"DH")

print ("-----------------------------")

S2=Salarie(1234,"chate","abd rafire",10000,0.25,E1)
S2.afficher_info2()
print("le salaire net est :",S2.SalaireNet(),"DH")

print ("-----------------------------")
