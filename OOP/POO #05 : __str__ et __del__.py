class etudian:
    def __init__(self,n=None,a=None):
        self.nom=n
        self.age=a

    # pour remplace la methode afficher 
    # E1.afficher ==> print(E1)   
    def __str__(self):
        return (f"le nom : {self.nom}, l'age : {self.age}")

     # pour afficher un message when : del E1  
    def __del__(self):
        print("ici la suprition de l'objet ")


E1=etudian("zeggaf",19)
print(E1)
del E1
