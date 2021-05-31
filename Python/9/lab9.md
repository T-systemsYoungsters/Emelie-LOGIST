```Python
#1
def min3(a,b,c):
    if a<=b:
        print(a)
    elif c<= a:
        print(c)
    elif b<=a:
        print(b)
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
def find(my_list, key):
    for key in range(len(my_list)):
        if my_list[key] ==key:
            print(key, "gefunden an der Position", my_list[key])
    
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

#4
import random
a=random.randrange(1,6)
my_list=[]
def create_list(5):
    my_list=create_list(5)
    for i in range(5):
        my_list.append(a)
        print(my_list)
    

