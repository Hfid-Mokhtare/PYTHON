class student: 
    def __init__(self,n="",a=""):
        self.Nam=n
        self.__age=a

    def get_age(self):
        return self.__age
    
    def set_age(self,n_age):
        self.__age=n_age  

    def del_age(self):
        del self.age

    def __str__(self):
        return self.Nam+" "+str(self.get_age())
    
    def __del__(self):
        print("the varible was delted :)")

    

S1=student(input("enter your name : "),input("enter your age : "))
print(S1)
S1.set_age(30)
print(S1)
