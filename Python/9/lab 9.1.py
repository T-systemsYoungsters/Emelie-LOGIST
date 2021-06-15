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
