from enum import Enum

class Favorit_Color(Enum):
    black=None
    white=None
    blue=None
    green=None

class MaritalStatus(Enum):
    married=1
    single=0

class Gender(Enum): 
    male=1
    femal=0


#here i Read the input from the user he will enter : married / single

Maritalsta=input("are you maride : (married / single)") 

if (Maritalsta==MaritalStatus.married.name):
    print("you are married :) \n")
else:
    print ("you are single :( \n")

#here i Read the input from the user he will enter : 1 / 0 

Maritalsta=int(input("are you maride : (1/0) ")) 

if (Maritalsta==MaritalStatus.married.value):
    print("you are married :) \n")
else:
    print ("you are single :( \n")
