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
