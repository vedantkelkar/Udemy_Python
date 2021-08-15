Ex1 Strings

firstn=input("What is your first name")
midn=input("What is your middle name")
lastn=input("What is your last name")

print("Initials are ",firstn[0],midn[0],lastn[0])    

code=input("Input the code")
print('Country Code',code[0:3])        
print('Product Code',code[4:9])        
print('Batch Code',code[10:])        

Ex Number

import math
rad=float(input("Input the radius"))
print("Circumference id",2*math.pi*rad)
print("Area is",math.pi*(rad**2))

Ex list and tuple

month=("Jan","Feb","March","april","may","june","july","august","sept","oct","Nov","Dec")
bday=input("Your Birthday")
ip=int(bday[3:5])-1
print("You were born in",month[ip])

li=["Vedant","Nachiket","Manas","Aakash","Aalap"]
newadd=input("What is your name")
max=li
max.append(newadd)
print(max)

Ex Dict

Dic={"name":"Vedant","age":9,"college":"KJ"}
print(Dic)
Dic["hobby"]="football"
print(Dic)
info=input("What info is needed")
print("Persons",info,"is",Dic[info])

Ex COnditions

Calculate BMI

height=float(input("Enter your height in meters"))
weight=float(input("Enter your weight in kilos"))
BMI=weight/(height*height)
print(BMI)

if BMI<=18.5:
    print("Under")
elif 18.5<BMI<=24.9:
    print("Normal")
elif 24.9<BMI<=29.9:
    print("Normal")
else:
    print("obese")

Ex loops

import random
names=[]
for i in range(0,4):
    name=input("Enter names")
    names.append(name)
    
print(names)
ind=random.randint(0,3)
rando=names[ind]
print(rando)

Guess game
import random
color=["red","blue","green","black"]
while True:
 guess=input("Enter your guess")
 ind=random.randint(0,len(color)-1)
 rando=color[ind]
 if guess==rando:
    print("GG")
    break
 elif guess!=rando:
    repeat=input("do you want to play again")
    if repeat=='yes':
        continue
    else:
        break
print("Game over")

Ex Modules

import time
print(time.localtime())
TIME=time.localtime()
print("Transacion complete at",str(TIME.tm_hour)+"h"+ str(TIME.tm_min)+"m")
print(time.localtime())

Ex MATPLOTLIB

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[100,200,300,400]
plt.plot(x,y)
plt.show()

Proj Time 
import matplotlib.pyplot as plt
import time as t

word=input("Word u want to type")
time=[]
mistake=0
initial=t.time()
for i in range(0,7):
 word1=input("The entered word")
 if word==word1:
    newtime=t.time()
    time.append(newtime)
 else:
    mistake=mistake+1
    newtime=t.time()
    time.append(newtime)
print(time)
print(newtime)
timereq=newtime-initial
print(mistake)
print(timereq)
x=time
x=[0,1,2,3,4,5,6]
y=[0,time[1]-time[0],time[2]-time[1],time[3]-time[2],time[4]-time[3],time[5]-time[4],time[6]-time[5]]
plt.plot(x,y)
plt.show()

a=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,9):
   if i==1 or i==4 or i==5 or i==8:
    print(a[i])       
