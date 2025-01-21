class student:
    group ="dev 101" 
    
    @classmethod 
    def AfficherClass(cls):
        print(cls.group)

    @staticmethod # C'est une methode de static
    def Somme(x,y):
        return x+y
    
    def __init__(self,name="",age=""):
        self.name=name
        self.age=age

    def afficher(self):
        print (self.__hello(),self.name," ",self.age," ")
        
student.AfficherClass()
print(student.Somme(10,20))

        
