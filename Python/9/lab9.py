import random

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
def find(my_list, key):
    for key in range(len(my_list)):
        if my_list[key] ==key:
            print(key, "gefunden an der Position", my_list[key])
    
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)


    
