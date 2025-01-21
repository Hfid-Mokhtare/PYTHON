from copy import copy

class EtreVivon:
    def __init__(self,type):
        self.type=type
    def __str__(self):
        return self.type
class person(EtreVivon): 
    def __init__(self,type, name,age):
        EtreVivon.__init__(self,type)
        self.name=name
        self.age=age
    def __str__(self):
        print("this is a class of person")

class student(person,EtreVivon):
    def __init__(self,type, name, age, school):
        EtreVivon.__init__(self,type)
        person.__init__(self,name, age)
        self.school=school
    def __str__(self):
        print ("this is a class of student qui h'irite de Etrevivon et person ")

S1=student(input("enter the type : "), input("enter the name : "), input("enter the age : "), input("enter the school name : "))
