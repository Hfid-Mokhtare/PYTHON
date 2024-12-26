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

    age=property(get_age,set_age,del_age)

S1=student(input("enter your name : "),input("enter your age : "))
print(S1)
S1.age=20
print(S1.age)
print(S1)


