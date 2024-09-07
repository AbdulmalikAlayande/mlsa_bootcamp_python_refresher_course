class InvalidAmountException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def get_message(self):
        return str(super().args[0])


class BankAccount:

    def __init__(
        self,
        account_number: str,
        pin: str,
        balance: float,
        is_suspended: bool,
        is_active: bool,
    ) -> None:

        self._account_number: str = account_number
        self._pin: str = pin
        self._balance: float = balance
        self._is_suspended: bool = is_suspended
        self._is_active: bool = is_active

    def withdraw(self, amount: int, pin):
        if amount <= 1000:
            raise InvalidAmountException(
                "You cannot withdraw an amount lesser than or equal to 1000"
            )
        else:
            print("hi")

    def __repr__(self) -> str:
        return f"""
        [
            Account Number: {self._account_number},
            Pin: {self._pin},
            Balance: {self._balance},
            Suspended: {self._is_suspended},
            Active: {self._is_active}
        ]
    """


if __name__ == "__main__":
    account = BankAccount("2395668018", "1932", 50.00, False, True)
    print(account)
    try:
        account.withdraw(500, "1968")
    except InvalidAmountException as exception:
        print("Error message==::>>", exception.get_message())
