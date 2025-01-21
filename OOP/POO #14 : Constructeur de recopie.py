from copy import copy

class group:
    def __init__(self,name="",filiere=""):
        self.name=name
        self.filiere=filiere

    def __str__(self):
        return self.name+"\n"+self.filiere

    def copy(self,g):
        self.name=g.name
        self.filiere=g.filiere

Gr1=group("Dev 101","front end")
print(Gr1)

# i will copy Gr1 to Gr2

Gr2=group()
Gr2.copy(Gr1)
print(Gr2)

# Gr2=copy(Gr1)  you can juste use this built in library
