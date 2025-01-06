def ReadPin():
    pin=input("Please enter the Pin : ")
    return pin


def CheckPin(pin):
    Balance=7500
    CorrectPin="1234"
    if pin == CorrectPin :
        print(f"Your Balance is : {Balance}")
    else:
        print("wrong Pin")

CheckPin(ReadPin())

# =============================================================

def ReadGrade():
    Grade=float(input("Please enter the the Grade : "))
    return Grade


def CheckGrade(Grade):
    if Grade >= 90 : 
       print('A')
    elif Grade >= 80:
       print('B')
    elif Grade >= 70:
       print('C')   
    elif Grade >= 60:
       print('D') 
    elif Grade >= 50:
       print('E')
    else :
       print('F')  

CheckGrade(ReadGrade())
