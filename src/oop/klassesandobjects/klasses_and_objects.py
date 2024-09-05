class Human:
    def __init__(self, name: str, age: int):
        self._name: str = name
        self._age: int = age

    def __str__(self) -> str:
        return f"""
        Name: {self._name}
        Age: {self._age}
        """


human = Human("sam", 45)
print(human)
