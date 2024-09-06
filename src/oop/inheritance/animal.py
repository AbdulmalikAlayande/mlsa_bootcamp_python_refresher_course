class Animal:

    def __init__(self, name: str, specie: str):
        self._name: str = name
        self._specie: str = specie

    def move(self) -> None:
        print("Moving Like An Animal")

    def sleep(self) -> None:
        print("I sleep like an Animal")

    def eat(self) -> None:
        print("I eat anything edible and delicious")

    def reproduce(self) -> None:
        print("I am an animal so I reproduce and multiply")

    def __str__(self) -> str:
        return "[Name: {name}, Specie: {specie}]".format(self._name, self._specie)


class WildCat(Animal):

    def hunt(self) -> None:
        print("I hunt preys because I am a predator")


class Fish(Animal):
    pass


class Bird(Animal):
    pass


class Insect(Animal):
    pass


eagle: Bird = Animal("Eagle", "Aves")
tuna: Fish = Animal("Tuna", "Pisces")
lion: WildCat = Animal("Lion", "Felidae")
cockroach: Insect = Animal("cockroach", "Insect")

# Eagle Demonstration
eagle.move()
eagle.sleep()
eagle.eat()
eagle.reproduce()
print(eagle)

print("=" for i in range(0, 20))
print("|" for i in range(0, 20))
print("=" for i in range(0, 20))

#
lion.move()
lion.sleep()
lion.eat()
lion.reproduce()
lion.hunt()
print(lion)

print("=" for i in range(0, 20))
print("|" for i in range(0, 20))
print("=" for i in range(0, 20))

# --------------------------------
tuna.move()
tuna.sleep()
tuna.eat()
tuna.reproduce()
print(tuna)

print("=" for i in range(0, 20))
print("|" for i in range(0, 20))
print("=" for i in range(0, 20))

# --------------------------------
cockroach.move()
cockroach.sleep()
cockroach.eat()
cockroach.reproduce()
print(cockroach)
