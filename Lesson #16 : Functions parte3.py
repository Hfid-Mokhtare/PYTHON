def Calcule_of_Power(Num,Power):
    return pow(Num,Power)

def PrintPowerResulte(result:int):
    print(result)

Num:float
Power:int 
Num=float(input("Please enter a number : "))
Power=int(input("Please enter the Power : "))

PrintPowerResulte(Calcule_of_Power(Num,Power))

#-------------------------------------------------------

import math

def Triagle_Area(Rib1:float,Rib2:float,Rib3:float):
    Pi:float=3.14
    P=(Rib1+Rib2+Rib3)/2
    return round(math.pi * pow(((Rib1 * Rib2 * Rib3) / (4 * math.sqrt(P * (P - Rib1) * (P - Rib2) * (P - Rib3)))), 2))

def PrintTriagleArea(CercleArea:float):
    print ("the cercle area = ",CercleArea)

Rib1=float(input("Please enter the triangle rib A : "))
Rib2=float(input("Please enter the triangle rib B : "))
Rib3=float(input("Please enter the triangle rib C : "))

PrintTriagleArea(Triagle_Area(Rib1,Rib2,Rib3))
