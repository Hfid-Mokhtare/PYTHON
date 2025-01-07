def ReadNum():
    Num=int(input("enter the number : "))
    return Num
def PrintResult(Num):
    for i in range(1,Num+1):
        print(i)
PrintResult(ReadNum())

#---------------------------------------------

def ReadNum():
    Num=int(input("enter the number : "))
    return Num
def PrintResult(Num):
    for i in range(Num,0,-1):
        print(i)
PrintResult(ReadNum())

#---------------------------------------------

def ReadNum():
    Num=int(input("enter the number : "))
    return Num
def PrintSumOddNumbers(Num):
    SumOddNum=0
    for i in range(1,Num+1,2):
        SumOddNum+=i
    print(SumOddNum)

PrintSumOddNumbers(ReadNum())

#---------------------------------------------

def ReadNum():
    Num=int(input("enter the number : "))
    return Num
def PrintSumEvenNumbers(Num):
    SumEvenNum=0
    for i in range(0,Num+1,2):
        SumEvenNum+=i
    print(SumEvenNum)

PrintSumEvenNumbers(ReadNum())
#---------------------------------------------


def ReadNum():
    Num=int(input("enter the number : "))
    return Num
def PrintSumFactorialNumbers(Num):
    Factorial=1
    for i in range(Num,0,-1):
        Factorial*=i
    print(Factorial)

PrintSumFactorialNumbers(ReadNum())

#---------------------------------------------

def ReadNum():
    Num=int(input("enter the number : "))
    Base=int(input("enter the base : "))
    return Num, Base

def PrintPowerOfNum(Num,Base):
    Power=1
    for i in range(1,Base+1):
        Power*=Num
    print(Power)
Num,Base=ReadNum()
PrintPowerOfNum(Num,Base)

#---------------------------------------------

def PrintLetters():
    for i in range(65,90+1):
        print(chr(i))


PrintLetters()




