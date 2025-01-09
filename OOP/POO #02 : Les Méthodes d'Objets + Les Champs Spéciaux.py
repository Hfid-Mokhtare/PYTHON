class student:
    def __init__(self,n="",p="",a=0): 
        self.nom=n # Attribu du class
        self.prenom=p 
        self.age=a
        
    def Afficher(self): # Creer une methode de Clase
        print(f"nom : {self.nom} , prenom : {self.prenom} , age : {self.age}")
        

S1=student("Zeggaf","Mohamed Ali",20) #
S1.Afficher()

S1.filier="DEV" # Attribu d'objet
# L'attribut speciaux
# .__dict__ : pour afficher tous les attribu de class avec les valeur
print(S1.__dict__)
# dir() : pour afficher les champ (les methode et les attribu ) de class 
print(dir(S1))
