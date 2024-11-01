class Employee:
    """
    Classes allow you to create user defined data structures
    Classes have functions, which are called methods, which identify the behaviours and actions that an object
    created from the class can perform with its data.
    """
    def __init__(self, name="Generic Doggo", age=2):
        self.name = name
        self.age = age

class Dog:
    """
    Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object/’s properties. 
    That is, .__init__() initializes each new instance of the class. __init__ and __str__ are dunder methods
    """
    species = "Canis Familiaris" # class attributes
    def __init__(self, name="Generic Doggo", age=2):
        self.name = name # instance attributes
        self.age = age # instace attributes

    def bark(self):
        return "Bhow Bhow"

    def __str__(self):
        return f"Hello Hooman, my name is {self.name} and I am {self.age} years old "

class Puppy(Dog):
    def __init__(self,name,age):
        super().__init__(name, age)
        

doggo1 = Dog("Edgar",8)
doggo2 = Dog("Pingu", 2)
doggo3 = Dog("Pablo",3)
doggo4 = Dog("Chocobar",3)
doggo5 = Dog()

print(doggo5.bark())

pup1 = Puppy("pingu2", 2)
print(pup1)

doggo5.name = "Miles"
print(doggo5)
    


    

