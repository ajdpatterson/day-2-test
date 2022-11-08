# define a non-empty tuple
car = ("BMW", "1 Series", "Black", 2000)
car_2 = "Audi", "A5", "Blue", 3000

# define an empty tuple
empty_tuple = ()
empty_tuple = tuple()

# access value in tuple
model = car[1]

# Can't modify though!

# car[1] = "Focus"

print(car)
print(car_2)
print(type(car))

print(model)

# count tuple elements
# tuple_count = len(car)
# print(tuple_count)

fruits = ("apple", "apple", "peach", "banana",)
print(fruits.count("apple")) 

print(car.count(2000))

# tuple of a single element
single_tuple = ("Andrew",)