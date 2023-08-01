# Use the values() method to create a list of items from a dictionary.
my_dict = {"apple": 1, "banana": 2, "orange": 3}
values_list = list(my_dict.values())
print(values_list)

# Check if a specific key exists in a dictionary.
if "apple" in my_dict:
    print("Key 'apple' exists in the dictionary.")

# Change and update items in a dictionary.
my_dict["banana"] = 4
print(my_dict)

# Add and remove items from a dictionary.
my_dict["grape"] = 5
print(my_dict)

del my_dict["orange"]
print(my_dict)

# Demonstrate looping through a dictionary and nesting dictionaries within dictionaries.
nested_dict = {"outer": {"inner": 1}}
for key, value in nested_dict.items():
    print(key, value)
    if isinstance(value, dict):
        for inner_key, inner_value in value.items():
            print(inner_key, inner_value)

# Determine the length of a string using the len() function.
my_string = "Kazibwe Julius"
print(len(my_string))

# Iterate through each character in a string using a for loop.
for char in my_string:
    print(char)

# Slice a string to extract specific portions of it.
sliced_string = my_string[8:12]
print(sliced_string)

# Perform arithmetic operations with numbers and print the results.
num1 = 10
num2 = 5
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Use boolean values and conditions to control program flow.
is_raining = False
if is_raining:
    print("Remember to take an umbrella.")
else:
    print("No need for an umbrella.")
