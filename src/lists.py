user_database: [{}] = []

user_1: dict = {
    "name": "Abdulmalik",
    "age": 19,
    "email": "alaabdulmalik03@gmail.com",
    "height": 23.65
}

user_2: dict = {
    "name": "Emmanuel",
    "age": 30,
    "email": "emmanuel@gmail.com",
    "height": 200.54
}

user_3: dict = {
    "name": "Daniel",
    "age": 25,
    "email": "daniel@gmail.com",
    "height": 90.12
}

def create_user(user: dict) -> None:
    user_database.append(user)
    print(user_database)

def delete_user(value: dict | int, message: str=None) -> None:
    if isinstance(value, dict) and message is not None:
        user_database.remove(value)
        print(message, user_database)
    elif isinstance(value, int) and message is not None:
        user_database.pop(value)
        print(message, user_database)
    print(user_database)



create_user(user_1) #[{'name': 'Abdulmalik', 'age': 19, 'email': 'alaabdulmalik03@gmail.com', 'height': 23.65}]
create_user(user_2) #[{'name': 'Abdulmalik', 'age': 19, 'email': 'alaabdulmalik03@gmail.com', 'height': 23.65}, {'name': 'Emmanuel', 'age': 30, 'email': 'emmanuel@gmail.com', 'height': 200.54}]
create_user(user_3) #[{'name': 'Abdulmalik', 'age': 19, 'email': 'alaabdulmalik03@gmail.com', 'height': 23.65}, ]

delete_user(user_1, "Deleted User 1") #[{'name': 'Emmanuel', 'age': 30, 'email': 'emmanuel@gmail.com', 'height': 200.54}, {'name': 'Daniel', 'age': 25, 'email': 'daniel@gmail.com', 'height': 90.12}]
delete_user(1, "Deleted User at index 1") #[{'name': 'Emmanuel', 'age': 30, 'email': 'emmanuel@gmail.com', 'height': 200.54}]