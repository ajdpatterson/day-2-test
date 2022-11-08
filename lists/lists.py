# create empty lists
empty_1 = []
empty_2 = list()

# create list with items
fruits = ["Apple", "Banana", "Orange"]

# reassign value at index

fruits[1] = "plum"
print(fruits[1])

# get the number of items
num_of_fruits = (len(fruits))
print(num_of_fruits)

# remove last element
removed_fruit = fruits.pop()
print(f"I removed {removed_fruit}")

# add a new fruit
fruits.append("strawberry")
print(f"I added {fruits[-1]}")
print(f"Fruits: {fruits}")