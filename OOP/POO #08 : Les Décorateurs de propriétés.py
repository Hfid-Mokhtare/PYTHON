class etudian:
    def __init__(self,n=None,a=None):
        self.nom=n
        # attribue privee
        self.__age=a
       
       
    # le nom de la fonction doit etre comme le nom de l'attribu priver pour reutilser
    @property
    def Age(self):
        return self.__age 

    @Age.setter
    def Age(self,n_value):
        self.__age = n_value

    @Age.deleter
    def Age(self):
        del self.__age

    def __str__(self):
        return f"le nom : {self.nom}, l'age : {self.__age}"

   
 
E1=etudian("zeggaf",19)
print(E1)

# modifier l'age
E1.Age=20
print(E1)

# Afficher age
print(E1.Age)
