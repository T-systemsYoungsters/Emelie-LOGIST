1)
 ```Python
for i in range(10):
    print("Emelie")
print("Done")
```
2)
```Python
for i in range(10):
    print("red")
    print("gold")
```
3) 
```Python
for i in range(2, 101, 2):
    print(i)
``` 
4)
```Python
i=10
while i>-1:
    print(i)
    i=i-1
print("Blast off!")
```
5)
```Python
print("This program takes three numbers and returns the sum.")
total = 0
 
for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x
print("The total is:", total)
```
6)
```Python
import random
my_number = random.randrange(1, 11)
print(my_number)
```
7)
```Python
import random
my_number= random.random()*1+9 #ändern
print(my_number)
```
8)
```Python
sum=0
total_positiv=0
total_zero=0
total_negativ=0
for i in range(7):
    x=int(input("Enter a number: "))
    sum= sum + x
    if x > 0:
        total_positiv = total_positiv +1
    elif x == 0:
        total_zero= total_zero +1
    else:
        total_negativ= total_negativ +1

        
print("The total is:", sum)
print("You entered a total of positiv numbers of:", total_positiv)
print("You entered a total of zeros of:", total_zero)
print("you entered a total of negativ numbers of: ", total_negativ)
```
9)
```Python
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

```
10)
```Python
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
    ```


