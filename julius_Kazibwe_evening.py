# Exercise 1
# Create a list with 5 items (French names of people) and output the 2nd item:
names = ["Jean", "Pierre", "Claire", "Marie", "Luc"]
print(names[1])  # Output: Pierre

# Change the value of the first item to a new value:
names[0] = "Louis"
print(names)  # Output: ['Louis', 'Pierre', 'Claire', 'Marie', 'Luc']

# Add a sixth item to the list:
names.append("Sophie")
print(names)  # Output: ['Louis', 'Pierre', 'Claire', 'Marie', 'Luc', 'Sophie']

# Add "Bathel" as the 3rd item in your list
names.insert(2, "Bathel")
print(names)  # Output: ['Louis', 'Pierre', 'Bathel', 'Claire', 'Marie', 'Luc', 'Sophie']

# Remove the 4th item from the list:
del names[3]
print(names)  # Output: ['Louis', 'Pierre', 'Bathel', 'Marie', 'Luc', 'Sophie']

# Use negative indexing to print the last item in your list:
print(names[-1])  # Output: Sophie

# Create a new list with 7 items and print the 3rd, 4th, and 5th items:
new_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape']
print(new_list[2:5])  # Output: ['Cherry', 'Date', 'Elderberry']

# Create a list of countries and make a copy of it:
countries = ['USA', 'Canada', 'France', 'Germany', 'Australia']
countries_copy = countries.copy()
print(countries_copy)

# Loop through the list of countries:
for country in countries:
    print(country)

# Sort a list of animal names in both descending and ascending order
animal_names = ['Zebra', 'Elephant', 'Lion', 'Tiger', 'Giraffe']
animal_names.sort()  # Ascending order
print(animal_names)  # Output: ['Elephant', 'Giraffe', 'Lion', 'Tiger', 'Zebra']


animal_names.sort(reverse=True)  # Descending order
print(animal_names)  # Output: ['Zebra', 'Tiger', 'Lion', 'Giraffe', 'Elephant']

# Output only animal names with the letter 'a' in them:

for name in animal_names:
    if 'a' in name.lower():
        print(name)

# Join two lists containing first and second names
first_names = ['Julius', 'Trevor', 'Michael', 'Emma']
last_names = ['Kazibwe', 'Ssemwogerere', 'Johnson', 'Williams']

full_names = []
for first, last in zip(first_names, last_names):
    full_names.append(f"{first} {last}")

print(full_names)

#Exercise 2
# Output your favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])  # Output: iphone

# Use negative indexing to print the 2nd last item in the tuple
print(x[-2])  # Output: tecno

# Update "iphone" to "itel" in the phones list
phone_list = list(x)
phone_list[1] = "itel"
x = tuple(phone_list)
print(x)  # Output: ('samsung', 'itel', 'tecno', 'redmi')

# Add "Huawei" to the tuple:

x = x + ("Huawei",)
print(x)  # Output: ('samsung', 'itel', 'tecno', 'redmi', 'Huawei')

# Loop through the tuple
for phone in x:
    print(phone)

# Remove the first item in the tuple
x = x[1:]
print(x)  # Output: ('itel', 'tecno', 'redmi', 'Huawei')

# Create a tuple of cities in Uganda using the tuple() constructor
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print(cities)

# Unpack your tuple
brand1, brand2, brand3, brand4 = x
print(brand1, brand2, brand3, brand4)

# Print the 2nd, 3rd, and 4th cities in the tuple
print(cities[1:4])  # Output: ('Entebbe', 'Jinja', 'Gulu')

#Join two tuples containing first and second names:
first_names = ("John", "Jane", "Michael")
last_names = ("Doe", "Smith", "Johnson")

full_names = first_names + last_names
print(full_names)

# Create a tuple of colors and multiply it by 3:
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print(multiplied_colors)

# Count the number of times 8 appears in the tuple (1, 3, 7, 8, 7, 5, 4, 6, 8, 5):
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)  # Output: 2

# Exercise 3
# initialize a set called beverages
beverages = set(["coffee", "tea", "juice"])
print(beverages)

# Add 2 more items to the beverages set
beverages.update(["water", "soda"])
print(beverages)  # Output: {'coffee', 'juice', 'water', 'soda', 'tea'}

# Check if "microwave" is present in the set

mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# Remove "kettle" from the set
mySet.remove("kettle")
print(mySet)  # Output: {'oven', 'microwave', 'refrigerator'}

#Loop through the set
for item in mySet:
    print(item)

# Add elements in a list to elements in a set
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)  # Output: {1, 2, 3, 4, 5, 6}

# Join two sets containing ages and first names
ages = {16, 19}
first_names = {"Ken", "David"}
joined_set = ages.union(first_names)
print(joined_set)

# Exercise 4
# Concatenate an integer and a string

num = 2
string = "apples"
result = str(num) + string
print(result)  # Output: 2apples

# Remove spaces at the beginning, in the middle, and at the end of a string
txt = "   Hello, Uganda!   "
result = txt.strip()
print(result)  # Output: "Hello, Uganda!"

# Convert the value of 'txt' to uppercase
txt = "Hello, Uganda!"
result = txt.upper()
print(result)  # Output: "HELLO, UGANDA!"

# Replace character 'U' with 'V' in a string:
txt = "Hello, Uganda!"
result = txt.replace('U', 'V')
print(result)  # Output: "Hello, Vganda!"

# Return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
result = y[1:4]
print(result)  # Output: " am"

# Correct the code to remove the error
x = 'All "Data Scientists" are cool!' # In this case, I removed the outermost quotation marks to fix the error.
print(x)  # Output: All "Data Scientists" are cool!


# Exercise 5
# Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print(Shoes["size"])  # Output: 40

# Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print(Shoes)  # Output: {'brand': 'Adidas', 'color': 'black', 'size': 40}

# Add a key/value pair "type": "sneakers" to the dictionary

Shoes["type"] = "sneakers"
print(Shoes)  # Output: {'brand': 'Adidas', 'color': 'black', 'size': 40, 'type': 'sneakers'}

# Return a list of all the keys in the dictionary

keys = list(Shoes.keys())
print(keys)  # Output: ['brand', 'color', 'size', 'type']

# alternative 
keys = list(Shoes)  # Using the dictionary itself as an iterable
print(keys)  # Output: ['brand', 'color', 'size']


# Return a list of all the values in the dictionary
values = list(Shoes.values())
print(values)  # Output: ['Adidas', 'black', 40, 'sneakers']

# Check if the key "size" exists in the dictionary
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

# Loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

# alterrnative 
for key in Shoes:
    print(key, ":", Shoes[key])


# Remove "color" from the dictionary
del Shoes["color"]
print(Shoes)  # Output: {'brand': 'Adidas', 'size': 40, 'type': 'sneakers'}

# Empty the dictionary
Shoes.clear()
print(Shoes)  # Output: {}

# Create a dictionary and make a copy of it
original_dict = {"name": "John", "age": 25}
copied_dict = dict(original_dict)
print(copied_dict)  # Output: {'name': 'John', 'age': 25}

# Show nested dictionaries
data = {
    "person1": {
        "name": "John",
        "age": 25
    },
    "person2": {
        "name": "Jane",
        "age": 30
    }
}

for person, details in data.items():
    print("Person:", person)
    for key, value in details.items():
        print(key, ":", value)
    print()
