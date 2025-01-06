# original and olde methode ------------------------
def ReadGrades(Grades):
    Grades.append(float(input("Please enter Grade 1 : ")))
    Grades.append(float(input("Please enter Grade 2 : ")))
    Grades.append(float(input("Please enter Grade 3 : ")))



def CalculeTheGrade(Grades):
    return (Grades[0]+Grades[1]+Grades[2])/3


def PrintResulte(Moyen:float):
    print("*"*50)
    print(f"the average of grades is : {Moyen}\n")

Grades=[]
ReadGrades(Grades)
PrintResulte(CalculeTheGrade(Grades))

# moderne methode in python ------------------------

def ReadGrades():
    Grades=[]
    for i in range(3):
        grade=float(input(f"Please enter Grade {i+1} : "))
        Grades.append(grade)
        
    return Grades

def CalculeTheGrade(Grades):
    return sum(Grades) / len(Grades)


def PrintResulte(Moyen:float):
    print("*"*50)
    print(f"the average of grades is : {Moyen}\n")

Grades=ReadGrades()
PrintResulte(CalculeTheGrade(Grades))


