class student:
    group ="dev 101" # C'est un atribut de class
    
    @classmethod # C'est une methode de class
    def AfficherClass(cls):
        print(cls.group)

    @classmethod
    def Somme(cls,x,y):
        return x+y
    
    def __init__(self,name="",age=""):
        self.name=name
        self.age=age

    def afficher(self):
        print (self.__hello(),self.name," ",self.age," ")
        
student.AfficherClass()
print(student.Somme(10,20))

        
