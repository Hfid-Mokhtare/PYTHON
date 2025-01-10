class etudian:
    def __init__(self,n=None,a=None,m=None,note=None):
        self.nom=n
        self.age=a
        
        # attribue privee
        self.__matricule=m 

        # attribue protejet
        self._note=note

    # accesseur : getter
    def get_matricule(self):
        return self.__matricule 

    # modificateur : setter
    def set_matricule(self,n_value):
        self.__matricule = n_value

    def __str__(self):
        return f"le nom : {self.nom}, l'age : {self.age}, la matricule : {self.__matricule}"

   
 
E1=etudian("zeggaf",19,"AAB",17)
print(E1)
print(f"la matricule est : {E1.get_matricule()}")
E1.set_matricule("ACC")
print(E1)
