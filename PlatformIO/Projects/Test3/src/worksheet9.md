PART 1
1.
```Python
for i in range(5):
    print(i + 1)
```
GUESS:1,2,3,4,5     ACTUAL: 1,2,3,4,5

2.
```Python
for i in range(5):
    print(i)
    i = i + 1
```
GUESS:0,1,2,3,4     ACTUAL: 0,1,2,3,4

3.
```Python
x = 0
for i in range(5):
    x += 1
print(x)
```
GUESS:1,2,3,4,5     ACTUAL:5

4.
```Python
x = 0
for i in range(5):
    for j in range(5):
        x += 1
print(x)
```
GUESS: 5,10,15,20,25    ACTUAL: 25

5.
```Python
for i in range(5):
    for j in range(5):
        print(i, j)
```
GUESS: 5,10,15,20,25    ACTUAL:0 0 0 1 0 2 0 3 0 4 1 0 1 1 1 2 1 3 1 4 2 0 2 1 2 2 2 3 2 4 3 0 3 1 3 2 3 3 3 4 4 0 4 1 4 2 4 3 4 4

6.
```Python
for i in range(5):
    for j in range(5):
        print("*", end="")
        print()
```
GUESS: 0* 0 0* 1 0* 2 0* 3 0* 4 1* 0 1* 1 1* 2 1* 3 1* 4 2* 0 2* 1 2* 2 2* 3 2* 4 3* 0 3* 1 3* 2 3* 3 3* 4 4* 0 4* 1 4* 2 4* 3 4* 4     ACTUAL:* * * * * * * * * * * * * * * * * * * * * * * * * * * (untereinander)

7.
```Python
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
```
GUESS:      ACTUAL: *****
                    *****
                    *****
                    *****
                    *****

8.
```Python
for i in range(5):
    for j in range(5):
        print("*", end="")
print()
```
GUESS:      ACTUAL:*************************

9.
```Python
# This is supposed to sum a list of numbers
# What is the mistake here?
my_list = [5, 8, 10, 4, 5]
i = 0
for i in my_list:
    i = i + my_list[i]
print(i)
```
GUESS:      ACTUAL: Fehler der List index ist außerhalb des Bereiches

10.
```Python
for i in range(5):
    x = 0
    for j in range(5):
        x += 1
print(x)
```
GUESS:1,2,3,4,5     ACTUAL: 5

11.
```Python
import random
play_again = "y"
while play_again == "y":
    for i in range(5):
        print(random.randrange(2), end="")
    print()
    play_again = input("Play again? ")
print("Bye!")
```
GUESS: solange y gedrückt wird werden 5 beliebige zahlen ausgegeben zwischen 1 und 0        ACTUAL: identisch mit GUESS außer das bei einer anderen eingabe außer y Bye ausgegeben wird

12.
```Python 
def f1(x):
    print(x)
y = 3
f1(y)
```
GUESS: x        ACTUAL: 3

13.
```Python
def f2(x):
    x = x + 1
    print(x)
y = 3
f2(y)
print(y)
```
GUESS:3     ACTUAL: 4 3

14.
```Python
def f3(x):
    x = x + 1
    print(x)
x = 3
f3(x)
print(x)
```
GUESS:4 3     ACTUAL: 4 3

15.
```Python
def f4(x):
    z = x + 1
    print(z)
x = 3
f4(x)
print(z)
```
GUESS: 4 4      ACTUAL: 4 und error

16.
```Python
def foo(x):
    x = x + 1
    print("x=", x)
 
x = 10
print("x=", x)
foo(x)
print("x=", x)
```
GUESS: 10, 11,11        ACTUAL: 10, 11, 10

17.
```Python
def f():
    print("f start")
    g()
    h()
    print("f end")
 
def g():
    print("g start")
    h()
    print("g end")
 
def h():
    print("h")
 
f()
```
GUESS: f start und danach error     ACTUAL: f start g start h g end h f end

18.
```Python
def foo():
    x = 3
    print("foo has been called")
 
x = 10
print("x=", x)
foo()
print("x=", x)
```
GUESS: x= 10, foo has been called, x= 10      ACTUAL:x= 10, foo has been called, x=10

19.
```Python
def a(x):
    print("a", x)
    x = x + 1
    print("a", x)
 
x = 1
print("main", x)
a(x)
print("main", x)
 
def b(y):
    print("b", y[1])
    y[1] = y[1] + 1
    print("b", y[1])
 
y=[123, 5]
print("main", y[1])
b(y)
print("main", y[1])
 
def c(y):
    print("c", y[1])
    y = [101, 102]
    print("c", y[1])
 
y = [123, 5]
print("main", y[1])
c(y)
print("main", y[1])
```
GUESS: main 1, a 1, a 2, main 1, main 123, b 123, b 124, main 123, main 123, c 123, c101, main 123      ACTUAL: main 1, a 1, a 2, main 1, main 5, b5, b6, main 6, main 5, c 5, c 102, main 5

PART 2

1.
```Python
def sum(a, b, c):
    return a + b + c
 
print(sum(10, 11, 12))
```

2.
```Python
def increase(x):
    return x + 1
 
x = 10
print("X is", x, " I will now increase x." )
print("X is now", increase(x))
```

3.
```Python
def print_hello():
    print("Hello")
 
print_hello()
```

4.
```Python
def count_to_ten():
    for i in range(11):
        print(i)
 
count_to_ten()
```

5.
```Python
def sum_list(list):
    sum = 0
    for i in list:
        sum+= i
    return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))
```

6.
```Python
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[(i+ 1)* -1]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))
```

7.
```Python
def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)
```

PART 3

```Python
#1 Write a function that prints out ``Hello World.''
def helloworld():
    print("Hello World")

#2 Write code that will call the function in the prior problem. 
helloWorld()

#3 Write a function that prints out ``Hello Bob'', and will take a parameter to let the caller specify the name. Do not put an input statement inside the function! Use a parameter.
def helloPerson(name):
    print("Hello", name)

#4 Write code that will call the function in the prior problem. 
helloPerson("Bob")

#5 Write a function that will take two numbers as parameters (not as input from the user) and print their product (i.e. multiply them). 
def mult(a,b):
    print(a*b)

#6 Write code that will call the prior function. 
mult(23,26)

#7 Write a function that takes in two parameters. The first parameter will be a string named phrase. The second parameter will be a number named count. Print phrase to the screen count times.  
def printThings(phrase, count):
    for i in range(count):
        print(phrase)

#8 Write code to call the previous function. 
printThings("Hello",5)

#9 Write code for a function that takes in a number, and returns the square of that number. (
def squareNumber(x):
    return x*x

#10 Write code to call the function above and print the output. 
result = squareNumber(12)
print(result)

#11 Write a function that takes three numbers as parameters, and returns the centrifugal force
def centrifugalForce(m,r,w):
    return m*r*w**2

#12 Write code to call the function above and display the result. 
f=centrifuagalForce(3,4,5)
print(f)

#13 Write a function that takes a list of numbers as a parameter, and prints out each number individually using a for loop
def printNumbers(list):
    for item in list:
        print (item)


