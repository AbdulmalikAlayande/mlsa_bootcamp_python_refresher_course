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
    
    
class WildCat(Animal):
    
    def move(self) -> None:
        print("I walk on all fours ")
    
    def sleep(self) -> None:
        print("I sleep like a Wild Cat")

class Fish(Animal):
    pass

class Bird(Animal):
    pass

class Insect(Animal):
    pass


