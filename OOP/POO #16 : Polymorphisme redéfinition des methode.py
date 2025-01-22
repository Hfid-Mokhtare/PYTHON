class person:
    def __init__(self,fname, lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return self.fname+" "+self.lname


class etre_vivant:
    def __init__(self,Taille, voix):
        self.Taille=Taille
        self.voix=voix
    def __str__(self):
        return self.Taille+ " "+ self.voix

class student(person):
    def __init__(self, fname, lname, note):
        person.__init__(self, fname, lname)
        self.note=note
    def __str__(self):
        return super.__str__() + str(self.note)

class professeur(person, etre_vivant):
    def __init__(self, fn, ln, t, v, sal):
        person.__init__(self,fn, ln)
        etre_vivant.__init__(self,t, v)
        self.salaire=sal
    def __str__(self):
        return person.__str__(self)+" " +etre_vivant.__str__(self)+" "+ str(self.salaire)

P1=professeur("ali", "zeggaf","moyen","parler",1000)
print(P1)
