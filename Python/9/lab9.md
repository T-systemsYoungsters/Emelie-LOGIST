```Python
#1
def min3(a,b,c):
    if a<=b and a<=c:
        print(a)
    elif c<= a and c<=b:
        print(c)
    elif b<=a and b<=c:
        print(b)
    else:
        print("Das is ein Fehler")
min3(4, 7, 5)
min3(4, 5, 5)
min3(4, 4, 4)
min3(-2, -6, -100)
min3("Z", "B", "A")

#2
def box(height, width):
    for row in range(height):
        for j in range(width):
            print("*",end="")
        print()
    
box(7,5)  
print()   
box(3,2) 
print()   
box(3,10) 

#3
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
def find(liste, key):
    for i in range(len(liste)):
        if liste[i] ==key:
            print(key, "gefunden an der Position", i)
    
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

#4
import random

def create_list(x):
    mylist=[]
    for i in range(x):
        mylist.append(random.randrange(1,7))
    return mylist 

        
my_list=create_list(5)
print(my_list)

########################################################

def count_list(liste, x):
    count=0
    for i in range(len(liste)):
        if x ==liste[1]:
            count=count+1
    return count
                   
    
count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

###################################################

def average_list(liste):
    sum=0
    for i in range(len(liste)):
        sum= sum+liste[i]
    return (sum/len(liste))

    
avg = average_list([1,2,3])
print(avg)    

#############################################

import random

def create_list(x):
    mylist=[]
    for i in range(x):
        mylist.append(random.randrange(1,7))
    return mylist 

my_list=create_list(10000)
print(my_list)        



def count_list(liste, x):
    count=0
    for i in range(len(liste)):
        if x ==liste[i]:
            count=count+1
    return count
                      
count = count_list((my_list),1)
print("1: ",count)
count = count_list((my_list),2)
print("2: ",count)
count = count_list((my_list),3)
print("3: ",count)
count = count_list((my_list),4)
print("4: ",count)
count = count_list((my_list),5)
print("5: ",count)
count = count_list((my_list),6)
print("6: ",count)



def average_list(liste):
    sum=0
    for i in range(len(liste)):
        sum= sum+liste[i]
    return (sum/len(liste))

    
avg = average_list(my_list)
print("Durchschnitt:" ,avg)

