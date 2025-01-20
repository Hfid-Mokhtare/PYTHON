class student:
    group ="dev 101" # C'est un atribut de class
    
    def __init__(self,name="",age=""):
        self.name=name
        self.age=age

    def afficher(self):
        print (self.__hello(),self.name," ",self.age," ")
        
    def __hello(self): # C'est une methode priver utiliser sauf dons 
       return "Hello"  # la class
        


S1=student("ali", 19)
print(S1.name)

S1.afficher()

        
