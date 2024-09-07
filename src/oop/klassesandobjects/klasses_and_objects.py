class Human:

    def __init__(self, name: str, age: int, body_mass_index: float, date_of_birth: str, email: str, phone_number: str, nin: str, is_disabled: bool, height: float):
        self._name: str = name
        self._age: int = age
        self._body_mass_index: float = body_mass_index
        self._dateOfBirth: str = date_of_birth
        self._email: str = email
        self._phoneNumber: str = phone_number
        self._nin: str = nin
        self._is_disabled: bool = is_disabled
        self._height: float = height


    def eat(self, food: str) -> None:
        print("I am eating", food)

    def sleep(self) -> None:
        print("I am sleeping")

    def walk(self) -> None:
        print("I am walking")

    def swim(self) -> None:
        print("I am swimming")

    def breathe(self) -> None:
        print("I am breathing")

    def __str__(self):
        return f"""
        Name: {self._name}
        Age: {self._age}
        BMI: {self._body_mass_index}
        DOB: {self._dateOfBirth}
        Email: {self._email}
        Phone Number: {self._phoneNumber}
        NIN: {self._nin}
        Disabled: {self._is_disabled}
        Height: {self._height}
        """

if __name__ == '__main__':
    human: Human = Human(
    "Abdulmalik",
    14,
    34.5,
    "12-30-2008",
    "email@gmail.com",
    "08166641969",
    "3458UIOERT90FRT",
    False,
    30.67
    )
    print(human)