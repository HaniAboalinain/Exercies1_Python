# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:54:05 2019

@author: Hani
"""

import numpy as np

print("=================================Exercise one=========================")

zeros = np.zeros(10)
ones = np.ones(10)
fives = np.ones(10)*5

print(zeros , ones , fives  , sep="\n")


print("=================================Exercise two=========================")

arr1 = np.arange(30 , 71)
print(arr1)



print("===============================Exercise three=========================")

arr2 = np.arange(30 , 71 , 2)
print(arr2)

print("===============================Exercise four==========================")

arr3 = np.arange(27).reshape(3, 3, 3)
print(arr3)


print("=============================Exercise five============================")

arr4 = np.random.normal( 0 , 1 )
print(arr4) 


print("=============================Exercise six=============================")

arr5 = np.arange(48).reshape(3, 4, 4)
for i in arr5:
    for j in i:
        for k in j:
            print(k)
            
print("============================Exercuse seven============================")


arr6 = np.arange(0, 21)
for i in arr6:
    if i > 8 and i <= 15:
         arr6[i]  = i * -1
print(arr6)


print("============================Exercuse eight============================")


x = [1, 8, 3, 5]
y = np.random.randint(0, 11, 4)
multi_num = x * y
print(multi_num)


print("============================Exercuse nine=============================")

arr7 = np.array([[1,2,3],[4,5,6]])
print(arr7.shape , arr7 , sep="\n")


print("============================Exercise ten==============================")

arr8 = np.arange(27).reshape(3, 3, 3)
print(arr8)

print("============================Exercise eleven===========================")

a = np.array([9,-1,2,5])
b = np.array([1,-6,0,10])
c = np.array([[1,8,2,5],[3,1,7,9]])

print("a-b: ", a-b)						# [ 8  5  2 -5]
print("a*b: ", a*b)						# [ 9  6  0 50]
print("a.dot(b): ", a.dot(b)) 	 	 	# 65
print("a*2: ", a*2)						# [18 -2  4 10]
print("np.sin(a): ", np.sin(a)) 	 	# [ 0.41211849 -0.84147098  0.90929743 -0.95892427]
print("a<3: ", a<3)						# [False  True  True False]
print("a.sum(): ", a.sum()) 	 	 	# 15
print("a.sum(axis=0): ", a.sum(axis=0)) # 15
print("c.sum(): ", c.sum()) 	 	 	# 36
print("c.sum(axis=0): ", c.sum(axis=0)) # [ 4  9  9 14]
print("a.min(): ", a.min()) 			# -1
print("a.max(): ", a.max())				# 9
print("a.mean(): ", a.mean()) 	 	 	# 3.75
print("a average(): ", np.average(a)) 	# 3.75
print("a median(): ", np.median(a))  	# 3.5
print("a std(): ", np.std(a))  	 	 	# 3.6996621467371855
print("a var(): ", np.var(a)) 	 	 	# 13.6875
print("c.cumsum(): ", c.cumsum()) 	 	# [ 1  9 11 16 19 20 27 36]
print("a[1:2] : ", a[1:2])				# [-1]
print("a[2:] : ", a[2:])				# [2 5]
print("c[-1] : ", c[-1])				# [3 1 7 9]



print("============================Exercise twelve===========================")


import matplotlib.pyplot as plt

x = range(1, 50)
y = [value * 3 for value in x]

plt.plot(x, y, color="blue")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')

plt.show()

print("============================Exercise thirteen===========================")


x1 = [10,20,30]
y1 = [20,40,10]

x2 = [10,20,30]
y2 = [40,10,30]

plt.plot(x1 , y1 , label="Line 1")
plt.plot(x2 , y2 , label="Line 2")

plt.legend()
plt.title('Two or more lines on same plot with suitable legends')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()



print("============================Exercise fourteen===========================")

t = np.arange(0., 5., 0.2)
t2=t**2
t3=t**3

plt.plot(t, t, 'g--', t, t2, 'bs', t, t3, 'r^')
plt.title('Figure 14')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()


print("============================Exercise fiveteen===========================")

PL = ['Python','Java', 'PHP', 'JavaScript', 'C#', 'C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]

x = [i for i , _ in enumerate(PL)]
plt.bar(x, popularity,color=("red","black","green","blue","yellow","lightblue"))
#plt.xticks(x, PL)
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language")

plt.show()

