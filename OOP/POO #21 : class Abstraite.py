from abc import ABC, abstractmethod

class form(ABC): 
    def __init__(self, c):
        self.couloure=c
    @abstractmethod
    def surface(self):
        pass

    @abstractmethod
    def diametre(self):
        pass

class cercle(form):
    def __init__(self, r):
        self.rayon=r
    def surface(self):
        return self.rayon**2
    def diametre(self):
        return self.rayon*2

class carre(form):
    def __init__(self, cote):
        self.cote=cote
    def surface(self):
        return self.cote*self.cote
    def diametre(self):
        return self.cote*4

C1=carre(4)
print(C1.diametre())
