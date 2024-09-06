"""
Demonstration of inheritance in Python using a simple zoo example.

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
In this example, the 'Animal' class is the parent class, and various animal classes such as 'WildCat', 'Fish', 
'Bird', and 'Insect' inherit from it. These subclasses either inherit the methods of the parent class or define 
their own specific behavior, as seen in the 'WildCat' class.

Classes:
    Animal:
        Represents a generic animal with basic properties and behaviors such as movement, sleep, 
        eating, reproduction, and a string representation.

    WildCat(Animal):
        Represents a specific type of animal (WildCat) that inherits all behaviors of 'Animal' and adds 
        the ability to hunt.

    Fish(Animal), Bird(Animal), Insect(Animal):
        These classes represent specific types of animals that inherit the behaviors from the 'Animal' class 
        without introducing new methods or behavior.

Usage of Code:
    - The 'Animal' class defines common characteristics and behaviors shared by all animals.
    - The 'WildCat' class extends 'Animal' by introducing a new method 'hunt', specific to wildcats.
    - The 'Fish', 'Bird', and 'Insect' classes inherit the behaviors of 'Animal' without adding additional 
      behaviors.
    - Instances of these classes are created and demonstrate basic inheritance: each class can call the methods 
      of its parent class, and classes like 'WildCat' can also access their unique method.

Attributes in Animal:
    - name (str): The name of the animal.
    - specie (str): The species the animal belongs to.

Methods in Animal:
    - __init__(name: str, specie: str): Initializes the animal with its name and species.
    - move(): Prints the movement behavior of the animal.
    - sleep(): Prints how the animal sleeps.
    - eat(): Prints what the animal eats.
    - reproduce(): Prints how the animal reproduces.
    - __str__(): Returns a formatted string representing the animal's name and species.

Methods in WildCat:
    - hunt(): Prints a message indicating the wildcat's predatory behavior.

Demonstration:
    - 'eagle' (Bird), 'tuna' (Fish), 'lion' (WildCat), and 'cockroach' (Insect) are instantiated and demonstrate 
      inherited behaviors from the 'Animal' class.
    - 'lion' (WildCat) also demonstrates its unique 'hunt' behavior.
    - The script showcases how inheritance allows shared functionality to be reused while also allowing 
      extensions through subclass-specific methods.

Example of Basic Inheritance:
    WildCat inherits all basic behaviors from Animal and adds new functionality:
        lion = WildCat("Lion", "Felidae")
        lion.move()         # Inherited from Animal
        lion.hunt()         # Specific to WildCat

    Fish, Bird, and Insect inherit all behavior from Animal but don't add new functionality.
"""
