import random
total_heads=0
total_tails=0
for i in range(50):
    my_number=random.randrange(2)
    if my_number==0:
        print("heads")
        total_heads+=1
    if my_number==1:
        print("tails")
        total_tails+=1
print("You had a total of heads of" ,total_heads, "and you had a total of tails of" , total_tails)
