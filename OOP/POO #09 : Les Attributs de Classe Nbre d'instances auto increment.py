class student:
    group ="dev 101" # C'est un atribut de class
    __nbre_student=0
    def __init__(self,name="",age=""):
        self.name=name
        self.age=age
        student.nbre_student+=1 # auto incrament


S1=student("ali", 19)
S2=student("Mohamed", 118)
S3=student("rida", 20)

print(S1.name)
print(student.group) # pour afficher l'atribu de class
print(student.nbre_student)
        
