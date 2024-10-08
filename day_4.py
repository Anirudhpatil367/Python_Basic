#day
#sets - unordered uniqe collection of elemets  no duplicates are present
#it is extremely fast for lookpups
#anything under () is set
x=set()
#anything under {} is dictionary 
s={4,32,2,2}
s2={3,6,8,9,2}
#print(type({}))
#print(s)
#s.add(5)
#print(s)
#s.remove(2)
#print(s)
print(33 in s)

#union
print(s.union(s2))

#intersection
print(s.intersection(s2))

#difference
print(s.difference(s2))

##------------------

#dictionary- a key value pair it could be list or numbers

x={'key':4}
print(x['key'])

#add new key
x['key2']=5
x[2]=[2,2,4,7,8,1]
print(x)

#to find some key in dictionary
print('key in x')

#get all values in dictionary
print(x.values())
print(list(x.values()))

#list all keys

print(list(x.keys()))

#deleting the values
del x['key']
print(x)

for key,value in x.items():
    print(key,value)

#comprehensions
#one line intialization of list,dictionary,tuples etc

x=[x for x in range(5)]
print(x)

x=[x-2 for x in range (5)]
print(x)

x=[[0 for x in range(100)]for x in range(5)]
print(x)

x=[i for i in range(100)if i%5==0]
print(x)

#comprehension for dictionary
x={i:0 for i in range(100)if i%5==0}
print(x)
print(type(x))

#for tuples
x=tuple(i for i in range(100)if i%5==0)
print(x)
print(type(x))

#functions

def func():
    print('run')
    def func():
        print('hi')
    func()
func()

def func(x,y):
    print('run',x,y)
    return x*y,x/y
print(func(5,6))
#indexing 
r1,r2=func(5,6)
print(r1,r2)

def func(x,y,z=None):
    print('run',x,y,z)
    return x*y,x/y
print(func(5,6,7))
#indexing 
r1,r2=func(5,6,7)
print(r1,r2)

#unpack operator
def func(x):
    def func2(x):
        print(x)

    return func2

#print(func(3)())
x=func(3)
print(x)

def func(*args,**kwargs):
    pass
x=[1,23,236262,2727]
print(x)
print(*x)

def func(x,y):
    print(x,y)
pairs=[(1,2),(3,4)]

for pairs in pairs:
    func(*pairs)

#unpack with dictionary
def func(x,y):
    print(x,y)
pairs=[(1,2),(3,4)]

for pairs in pairs:
    func(**{'x':2,'y':5})

#note ** is used for dictionary and * is used for list,set,tuples
