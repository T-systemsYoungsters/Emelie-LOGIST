PART 1

1.What is the difference between a class and an object?
    Klasse: Oberbegriff für ein Objekt z.b: Person
    Objekt: Teilgebiet von der Klasse z.B: Horst, Anna

2.What is the difference between a function and a method?
    Funktion: Programmcode der gezielt aufgerufen werden muss, umfasst alle anweisungen was die Klasse beinhaltet
    Methode: beschreibt was Objekte tun können z.B: springen, klettern, tanzen

3.Write code to create an instance of this class and set its attributes. Remember, don't store numbers as strings. Use 40 and not "40".
```Python
class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0
Labrador=Dog()
Labrador.age=5
Labrador.name="Karl"
Labrador.weight=22
```

4.Write code to create two different instances of this class and set attributes for both objects. While a phone number is a number, those should be stored as strings. So we can keep leading zeros and those dashes.
```Python
class Person():
    def __init__(self):
        self.name = ""
        self.cell_phone = ""
        self.email = ""
Karl_person=Person()
Karl_person.name="Karl"
Karl_person.cell_phone="0123456789"
Karl_person.email="Karl.mustermann@gmail.com"

Hanna_person=Person()
Hanna_person.name="Hanna"
Hanna_person.cell_phone="9876543210"
Hanna_person.email="Hanna.musterfrau@gmail.com"
```

5.For the code below, write a class that has the appropriate class name and attributes that will allow the code to work.
```Python
class Bird()
    def __init__(self):
        self.colour = ""
        self.name = ""
        self.breed = ""

my_bird = Bird()
my_bird.color = "green"
my_bird.name = "Sunny"
my_bird.breed = "Sun Conure"
```

6.Define a class that would represent a character in a simple 2D game. Include attributes for the position, name, and strength.
```Python
class monster()
    def __init__(self):
        self.position=0
        self.name = ""
        self.strength = ""
```

7.The following code runs, but it is not correct. What did the programmer do wrong?
FALSCH: Es wurden unten nancy.name und nancy.money vergessen 
```Python
class Person():
    def __init__(self):
        self.name = ""
        self.money = 0
 
nancy = Person()
name = "Nancy"
money = 100

```

8.Take a look at the code. It does not run. What is the error that prevents it from running?
FALSCH: Es wurde bob.money vergessen
```Python
class Person():
    def __init__(self):
        self.name = ""
        self.money = 0
 
bob = Person()
print(bob.name, "has", money, "dollars.")
```

9.Even with that error fixed, the program will not print out:
Bob has 0 dollars.
Instead it just prints out:
has 0 dollars.
Why is this the case? 
Weil kein Name für ihn festgelegt wurde, nur das geld

10.Take pairs of the following items, and list some of the "has-a" relationships, and the "is-a" relationships between them. For example, if you were working with a different list, you might pull "Dolphin" and "Mammal" and then say "Dolphin is a Mammal." Please don't use items that aren't on the list.

    Checking account
    Person has a bank account, adress
    Customer is a person
    Bank Account is a checking account, mortgage account
    Transaction is a deposit, withdraw 

11.In Python, how is an ``is-a'' relationship implemented? Give an example of how it is implemented. 
    Mutter-,Tochterklassen 

12.In Python, how is a ``has-a'' relationship implemented? Give an example of how it is implemented.
    Klasse person kann ein Atribut Hund haben

13.How does this "has-a" relationship work if an object is allowed more than one item of a given type? For example, a Customer class might have an attribute for account. So a Customer "has-a" account. But what if a customer has two accounts? Or ten? How do you store any number of items? We learned this back in Chapter 7. How do we make an attribute that can hold more than one of a given type? (Ask if you aren't sure.)
    Mit einer Liste

PART 2

1.
```Python
class Animal():
    def __init__(self):
        self.name = ""
        print("A new animal has been born")

    def eat():
        print("Munch Munch")
 
    def make_noise():
        print("Grrr says[animal name].")
```

2.
```Python
class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("A cat has been born")

    def make_noise(self):
        print("Meow says", self.name_cat)
```
3.
```Python
class Dog(Animal):
    def __init(self):
        super().__init__()
        print("A dog has been born")

    def make_noise(self):
        print("Bark says" , self.name_dog)
```
4.
```Python
class Animal():
    def __init__(self):
        self.name = ""
        print(self.name, "A new animal has been born")

    def eat(self):
        print("Munch Munch")
 
    def make_noise(self):
        print("Grrr says", self.name)

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("A cat has been born")

    def make_noise(self):
        print("Meow says", self.name)

class Dog(Animal):
    def __init(self):
        super().__init__()
        print("A dog has been born")

    def make_noise(self):
        print("Bark says" , self.name)


a=Animal()
a.name="Ella"
a.eat()
a.make_noise()
print("---------------")

b=Cat()
b.name="Bernd"
b.eat()
b.make_noise()
print("---------------")

c=Dog()
c.name="Bello"
c.eat()
c.make_noise()
print("---------------")

c=Dog()
c.name="Hugo"
c.eat()
c.make_noise()
print("---------------")

```
