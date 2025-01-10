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

    # delete : setter
    def del_matricule(self):
        del self.__matricule

    # utiliser Les propriete : getter, setter, deletter, doc
    matricule=property(get_matricule, set_matricule, del_matricule, "matricule de l'etudian")

    def __str__(self):
        return f"le nom : {self.nom}, l'age : {self.age}, la matricule : {self.__matricule}, la note : {self._note}"

   
 
E1=etudian("zeggaf",19,"AAB",17)
print(E1)

# modifier la matricule
E1.matricule="ACC"
print(E1)

# suprimer la matricule
del E1.matricule
print(E1) # il va donner une error car on suprimer la matricule
