def func(*args, **kwargs):
    print(args,kwargs)
func(1,2,3,4,5,one=0,two=1)

#here keyword arguments
#kwargs in Python is a special syntax that allows you to pass a keyworded, variable-length argument dictionary to a function. It is short for "keyword arguments". When defining a function, you can use the ** in front of a parameter to indicate that it should accept any number of keyword arguments.
#here args->12345
#kwargs(one=0,two=1)

#scope and global

x='tim'

def fucn(name):
    global x
    x=name
print(x)
func('changed')
print(x)
#exceptions

#raise Exception('bad')
#raise FileExistsError('')

try:
    x=7/0
except Exception as e:
    print(e)
finally:
    print('finally')

#lambda-one line anyonmys fucntion

x=lambda x,y:x+y

print(x(2,3))

#map and filter: make use of lambda

x=[1,2,4,5,6,7,8,9,0,12,14,15,16,17,28]
mp=map(lambda i:i+2,x)
print(list(mp))

#filter-return true and false 
x=[1,2,4,5,6,7,8,9,0,12,14,15,16,17,28]
mp=filter(lambda i:i%2==0,x)
print(list(mp))

#F String
tim=89
x=f'hello{7+9}{tim}{67+9}'
print(f'hello{tim}')