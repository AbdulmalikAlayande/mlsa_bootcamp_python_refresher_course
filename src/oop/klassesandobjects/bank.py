from typing import Dict

"""
the type int is to specify that the key of this dictionary should be int 
and the value should be a dictionary
"""
bank_users_db: Dict[int, Dict] = {}

bank_accounts_db: Dict[int, Dict] = {}

current_number_of_users_in_the_db: int = 0

current_number_of_accounts_in_the_db: int = 0


def create_user(user: dict) -> dict:
    user.id = current_number_of_users_in_the_db + 1
    bank_users_db[user.id] = user
    return user


def create_account(account: dict) -> dict | str:
    owner = bank_users_db.get(account.owner_id)
    if owner is not None:
        account.id = current_number_of_accounts_in_the_db + 1
        bank_accounts_db[account.id] = account
        return account
    else:
        return "User with the Id provided does not exist"


def deposit(account_id: int, amount: float) -> dict:
    account = bank_accounts_db.get(account.id)
    if account is not None:
        account.balance += amount
        return account
    else:
        return "Account with the Id provided does not exist"


def withdraw(account_id: int, amount: float, pin: int) -> dict:
    account = bank_accounts_db.get(account_id)
    if account is not None:
        if account.pin == pin and account.balance >= amount:
            account.balance -= amount
            return account
        else:
            return "Insufficient funds or Incorrect PIN"
    else:
        return "Account with the Id provided does not exist"



# Main

user_1 = {
    "name": "John Doe",
    "age": 30,
    "id" : 0,
}

account_1 = {
    "balance": 0,
    "owner_id": 1,
    "pin": 1234,
    "id": 0
}

created_user_1 = create_user(user_1)

created_account_1 = create_account(account_1)

print(created_user_1)
print(created_account_1)
