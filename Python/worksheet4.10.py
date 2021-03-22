import random
user=0
user_win=0
computer=0
computer_win=0
user=int(input("Please enter your number! 1 is rock, 2 is paper and 3 is scissor!"))
if user ==1:
    print("You choose: Rock!")
if user ==2:
    print("You choose: Paper!")
if user ==3:
    print("You choose: Scissor!")
computer=random.randrange(1,4)
if computer ==1:
    print("The Computer choose: Rock!")
if computer ==2:
    print("The Computer choose: Paper!")
if computer ==3:
    print("The Computer choose: Scissor!")
if user<computer:
    computer_win= computer_win+1
    print("The Computer won!")
if user>computer:
    user_win=user_win+1
    print("You won!")
if user==computer:
    print("This round no one won!")
