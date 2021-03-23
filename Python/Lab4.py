import random
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert:")
print("The natives wan their camel back and are chasing you down! Survive your desert trek and out run the natives.")
done = False
miles=0
thirst=0
tiredness=0
distance_natives=-20
drinks=5
distance=random.randrange(7,15)
sleep=random.randrange(1,4)
way=random.randrange(10,21)
way_two=random.randrange(5,13)
while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    choice=input("What is your choice?")
    print()
    if choice.upper()=="Q":
        done=True
    elif choice=="E":
        print("Miles traveled:", miles)
        print("Drinks in canteen:", drinks)
        print("The natives are", distance_natives, "miles behind you.")
        print()
    elif choice=="D":
        tiredness=0
        print("The camel is happy!")
        print()
        distance_natives=distance_natives + distance
    elif choice=="C":
        miles=miles + way
        print("You have traveled", miles, "miles")
        print()
        thirst= thirst+1
        tiredness= tiredness+ sleep
        distance_natives= distance_natives+ distance
    elif choice=="B":
        miles= miles + way_two
        print("You have traveled", miles, "Miles")
        print()
        thirst= thirst+1
        tiredness=tiredness+1
        distance_natives= distance_natives+ distance
    elif choice=="A":
        drinks=drinks-1
        thirst=0
        if drinks==0:
            print("Sorry no drinks left!")
            print()
    if thirst >4:
        print("You are thirsty.")
        print()
    elif thirst>6:
        print("You died of thirst!")
        done=True
    if tiredness>5:
        print("Your camel is getting tired.")
        print()
    elif tiredness>8:
        print("You camel died of tiredness!")
        done=True
    if distance_natives == miles:
        print("Game over! The natives caught you!")
        done=True
    elif distance_natives<=15>=miles:
        print("Natives are getting close!")
        print()
    if miles>=200:
        print("You won!")
        done=True
        oasis=random.randrange(1,21)
        chance=int(input("Enter a number bewtween 1 and 20. Maybe you are the lucky one who founds the oasis"))
        if chance==oasis:
            print("You found the Oasis, know you are fuul of luck!")
            canteen=5
            thrist=0
            tirdness=0
               
    
        
    
