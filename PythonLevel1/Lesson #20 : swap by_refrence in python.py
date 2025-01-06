
# using a temporary variable -------------------------
def SwapNumbers(num1:int, num2:int):
    Temp: int
    num1=num2
    Temp=num1
    num2=Temp
    return num2, num1

def PrintNumbers(num1:int, num2:int):
    print("number 1 is : ",num1)
    print("number 2 is : ",num2)


num1:int
num2:int

num1=int(input("enter the first number : "))
num2=int(input("enter the seconde number : "))

PrintNumbers(num1, num2)
num1, num2 = SwapNumbers(num1, num2)
PrintNumbers(num1, num2)

# the beste way to solve this problem in python is ----------------

num3:int
num4:int

num3=int(input("enter the thered number : "))
num4=int(input("enter the fourthe number : "))

PrintNumbers(num3, num4)

# swap numbers :
num3, num4 = num4, num3
PrintNumbers(num3, num4)


