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

