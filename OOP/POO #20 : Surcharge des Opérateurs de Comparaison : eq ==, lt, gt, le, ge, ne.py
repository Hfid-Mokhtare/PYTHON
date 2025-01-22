class poin:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "absice : "+ str(self.x)+" ordonne : "+str(self.y)
    def __add__(self,p):
        a=self.x+p.x
        b=self.y+p.y
        return (a,b)
    
    def __lt__(self,p): # lt : lower tha  | gt : grater than | le : lower equal | ge : grater equale | eq equale | ne : not equale
        return self.x<p.x

p1=poin(0, 20)
p2=poin(5, 7)
# p3 = p1.__add__(p2)
p3=p1+p2
print (p1)
print (p2)
print (p3)

if(p1<p2):
    print("the absice of p1 is lower than p2")


