"""
Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, and the classes that you derive child classes from are called parent classes.
You inherit from a parent class by creating a new class and putting the name of the parent class into parentheses:
"""


class Parent:
    hair_color = "brown"

class Child(Parent):
    pass
