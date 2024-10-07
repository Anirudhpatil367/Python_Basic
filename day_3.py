#collections 
#collection is an unordered  and ordered group of elements.
#x=[4,True,'hi']
#y='hi'
#print(len(x),len(y))

#append is used to add at the end of the list
#x=[4,True,'hi']
#x.append('hello')
#print(x)

#extend
#x=[4,True,'hi']
#x.extend('hello')
#print(x)

#pop
x=[4,True,'hi']
y=x.pop()
print(y)

# 0 -first element of the world and -1 is the last element
x=[4,True,'hi']
x[0]='hello'
print(x)
#--
x=[4,True,'hi']
y=x[:]# a copy is made
print(y)
x[0]='hello'
print(x,y)

#tuple same as list but we cannot mutate , we can append, we cannot remove
#x=(0,0,2,2)
#x.append(3)
#print(x)

#x=[[],(),[[],[],[3,4,5]]]
#print(x)


#loops
#while loops is running indefine times
#for i in range(10):
    #print(i)


#stop
#start,stop
#start, stop ,step
#for i in range(10,-1,-1):
 #   print(i)
#list in loops 
#for i in[3,4,42,3,2,4]:
 #   print(i)

#x=[3,4,42,3,2,4]
#for i in range(len(x)):
 #   print(x[i])

x=[3,4,42,3,2,4]
for i,element in enumerate(x):
    print(i,element)

#while condition==true
#x=[3,4,42,3,2,4]
#i=0
#while i<10:
 #   print('run')
  #  i=i+1

#--
#x=[3,4,42,3,2,4]
#i=0
#while True:
 #   print('run')
  #  i=i+1
   # while True:
    #    if i==10:
     #       break

#slice operator--take a slice of a collection
x=[0,1,2,3,4,5,6,7,8]
y=['hi','hello','ggodbye','cya','sure']
s="hello"
sliced=x[0:4:2]
#sliced=x[start:stop:step]
print(sliced)
#----
x=[0,1,2,3,4,5,6,7,8]
y=['hi','hello','ggodbye','cya','sure']
s="hello"
sliced=x[::-2]
#sliced=x[start:stop:step]
print(sliced)