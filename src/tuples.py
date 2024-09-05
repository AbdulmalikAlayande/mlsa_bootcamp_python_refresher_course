student_tuple = ("Samuel", "Jackson", 4.50)
food_tuple = ("Bread", "Akara", "Yam")

print(student_tuple)
print(food_tuple)

singleton_tuple = ('random-string',)
print(type(singleton_tuple))

print(student_tuple[1])
print(student_tuple[-3])

for index in range(0, len(food_tuple)):
    print(food_tuple[index])

tuple_of_integers = (20, -3, 9)
print(tuple_of_integers) # (20, -3, 9)
tuple_of_integers += (34, 89, 90)
print(tuple_of_integers) # (20, -3, 9, 34, 89, 90)



