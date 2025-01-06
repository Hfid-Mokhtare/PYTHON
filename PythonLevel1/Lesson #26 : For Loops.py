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


