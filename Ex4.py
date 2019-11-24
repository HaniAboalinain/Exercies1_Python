# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:18:32 2019

@author: Hani
"""

"""
print("==============================Q1==============================")

o = lambda x=1 , y=2 , z=3 , : x+y+z 
print(o())
print(o(10))
print(o(10,20))


print("==============================Q2==============================")

my_list1 = [1,2,3,4,5]
def multi (my_list):
    m = 1
    for i in my_list :
        m = m * i
    print("multiplay :" , m)

multi(my_list1)

print("==============================Q3==============================")

x = lambda a , b : a*b 
print(x(6,5))


print("==============================Q4==============================")



y = list(filter(lambda i : i < 0 and i % 2 == 1 , range(-5 , 5)))
print(y)


print("==============================Q5==============================")

x = lambda a,b,c : a+b+c 
print (x(5,6,2))

#OUTPUT = 13

print("==============================Q6==============================")

x = ("Joey" , "Monica" , "Rose")
y = ("Chandler" , "Pheobe")
z = ("David" , "Rachel" , "Country")
result = list(zip(x,y,z))
print(result)



OUTPUT = 
[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]


print("==============================Q7==============================")

coin = ('Bitcoin' , 'Ether' , 'Ripple' , 'Litecoin')
code = ('BTC' , 'ETH' , 'XRP' , 'LTC')
d = dict(zip(coin, code))
print(d)


OUTPUT = 
{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}



print("==============================Q8==============================")

#function that filters vowels

def fun(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False;

sequence = ['g' , 'j' , 'e' , 'j' , 'k' , 'o' , 'p' , 'r']
filtered = list(filter(fun, sequence))
print(filtered)


OUTPUT = ['e' , 'o']


print("==============================Q9==============================")

x = list(map(int , input("Enter a multiple value: ").split()))
print("list of students: ",x)


OUTPUT = 
list of students:  [1, 20, 10]



print("==============================Q10==============================")

def newfunc(a):
    return a*a
t=list(map(newfunc,(1,2,3,4)))
print(t)


OUTPUT = 
[1, 4, 9, 16]


print("==============================Q11==============================")

def func(a,b):
    return a+b
a= list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)


#OUTPUT = [3, 6, 8]

print("==============================Q12==============================")
c = map(lambda x: x+x , filter(lambda x :(x >= 3) , (1,2,3,4)))
print(list(c))

#OUTPUT [6,8]
print("==============================Q13==============================")
c = filter(lambda x: (x>=3) , map(lambda x:x+x , (1,2,3,4)))
print(list(c))

#OUTPUT = [4, 6, 8]

print("==============================Q14==============================")
import functools 
mylist = [0 ,  1 , 3, 5, 6, 2, ] 

print ("The minimum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a < b else b,mylist))


"""
print("==============================Q15==============================")
numbers = [1,2,3]
letters= ['a','b','c']
results = tuple(zip(numbers, letters))
print(results)



