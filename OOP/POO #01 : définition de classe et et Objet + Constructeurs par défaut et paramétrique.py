class student:
    def __init__(self): #constructeur par defaut d'initialisation
        self.nom=""
        self.prenom=""
        self.age=0

class person:
    def __init__(self,n="reda",p="",a=0): #constructeur parametrique
        self.nom=n
        self.prenom=p
        self.age=a

        

S1=student() # Creer une variable S1 et instancier lobjet S1
S1.nom="zeggaf"
S1.prenom="Mohamed Ali"
S1.age=19
print(f"nom : {S1.nom} , prenom : {S1.prenom} , age : {S1.age}")

P1=person("Zeggaf","Mohamed Ali",20) # Creer un variable P1 et instancier lobjer P1
P1.age=25
print(f"nom : {P1.nom} , prenom : {P1.prenom} , age : {P1.age}")

