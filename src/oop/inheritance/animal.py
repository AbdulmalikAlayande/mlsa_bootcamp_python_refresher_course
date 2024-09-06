class Animal:
    """
    The 'Animal' class represents a generic animal with common properties such as name and species,
    as well as basic behaviors like moving, sleeping, eating, and reproducing.

    Attributes:
        name (str): The name of the animal.
        specie (str): The species the animal belongs to.
    """

    def __init__(self, name: str, specie: str):
        """
        Initializes the animal with its name and species.

        Args:
            name (str): The name of the animal.
            specie (str): The species the animal belongs to.
        """
        self._name: str = name
        self._specie: str = specie

    def move(self) -> None:
        """
        Simulates the animal's movement. In this base class, it prints a generic message about movement.
        """
        print("Moving Like An Animal")

    def sleep(self) -> None:
        """
        Simulates the animal's sleep behavior by printing a message about how it sleeps.
        """
        print("I sleep like an Animal")

    def eat(self) -> None:
        """
        Prints a message about the animal eating food. The behavior is generic in the base class.
        """
        print("I eat anything edible and delicious")

    def reproduce(self) -> None:
        """
        Prints a message about the animal reproducing and multiplying.
        """
        print("I am an animal so I reproduce and multiply")

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the animal, showing its name and species.
        """
        return "[Name: {0}, Specie: {1}]".format(self._name, self._specie)


class WildCat(Animal):
    """
    The 'WildCat' class represents a specific type of animal (wildcat) that inherits from 'Animal'.
    It adds a new behavior: hunting, which is unique to wildcats.

    Inherits:
        Animal: All the basic behaviors (move, sleep, eat, reproduce) are inherited.
    """

    def hunt(self) -> None:
        """
        Prints a message specific to wildcats, indicating that they hunt prey.
        """
        print("I hunt preys because I am a predator")


class Fish(Animal):
    """
    The 'Fish' class inherits from 'Animal'. No new behaviors are added.
    It uses the default behaviors of an 'Animal'.
    """

    pass


class Bird(Animal):
    """
    The 'Bird' class inherits from 'Animal'. No new behaviors are added.
    It uses the default behaviors of an 'Animal'.
    """

    pass


class Insect(Animal):
    """
    The 'Insect' class inherits from 'Animal'. No new behaviors are added.
    It uses the default behaviors of an 'Animal'.
    """

    pass


# Example usage of the Animal, WildCat, Fish, Bird, and Insect classes:

eagle: Bird = Animal("Eagle", "Aves")
tuna: Fish = Animal("Tuna", "Pisces")
lion: WildCat = Animal("Lion", "Felidae")
cockroach: Insect = Animal("Cockroach", "Insect")

# Eagle Demonstration
eagle.move()
eagle.sleep()
eagle.eat()
eagle.reproduce()
print(eagle)
"""
The 'eagle' object is an instance of the 'Bird' class, which inherits all methods from 'Animal'.
It will use the 'move', 'sleep', 'eat', 'reproduce' methods defined in the parent class 'Animal'.
The '__str__' method will print its name and species.
"""

print("=" * 20)
print("|" * 20)
print("=" * 20)

# Lion Demonstration
lion.move()
lion.sleep()
lion.eat()
lion.reproduce()
lion.hunt()
print(lion)
"""
The 'lion' object is an instance of the 'WildCat' class, which inherits from 'Animal' but also has 
its own specific method 'hunt'. This demonstrates how subclasses can extend parent classes with 
new behaviors in inheritance.
"""

print("=" * 20)
print("|" * 20)
print("=" * 20)

# Tuna Demonstration
tuna.move()
tuna.sleep()
tuna.eat()
tuna.reproduce()
print(tuna)
"""
The 'tuna' object is an instance of the 'Fish' class, which inherits all behaviors from 'Animal'.
Since 'Fish' does not define any new behavior, it will only use the inherited methods.
"""

print("=" * 20)
print("|" * 20)
print("=" * 20)

# Cockroach Demonstration
cockroach.move()
cockroach.sleep()
cockroach.eat()
cockroach.reproduce()
print(cockroach)
"""
The 'cockroach' object is an instance of the 'Insect' class, which inherits all behaviors from 'Animal'.
It uses only the inherited methods from 'Animal'.
"""
