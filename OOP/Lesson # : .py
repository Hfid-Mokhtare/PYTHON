from collections import namedtuple, Counter, deque, defaultdict, ChainMap

#NamTyple = namedtuple('NamTuple',['champ1','champ2',...])
Point = namedtuple("point",['x','y'])
p = Point(10,20)
print(p.x, p.y)
p2= Point(30, 50)
print(p2.x, p2.y)


#### ####
data = ['a', 'b','b','c','a','a','b']
counter= Counter(data)
print(counter)

######## d= deque(iterable, maxlen) 


de = deque([1,2,3])
de.append(4)
de.appendleft(0)
print(de)

de.pop()
de.popleft()
print(de)

# d = deque([1,2,3], maxlen=3)


###  cm = ChainMap(dict1,dict2,...)  ####
print ("-"*50)
d1 = {'prenom': 6, 'age':20}
d2 = {'x':5,'Y':10}
cm = ChainMap(d1,d2)
print(cm['age'])
print(cm['x'])
print(cm['prenom'])
print(cm['Y'])
