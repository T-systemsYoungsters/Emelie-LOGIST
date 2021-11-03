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
        
    
