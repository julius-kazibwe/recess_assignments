try:
    # SyntaxError: Missing colon in the if statement
    # if True
    #     print("SyntaxError: Missing colon")

    # # TypeError: Adding string and integer
    # result = "Hello" + 5

    # # NameError: Using an undefined variable
    # print(undefined_variable)

    # IndexError: Accessing an out-of-range index
    numbers = [1, 2, 3]
    print(numbers[3])

    # KeyError: Accessing a non-existent key in a dictionary
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])

    # ValueError: Converting an invalid string to an integer
    number = int("abc")

    # AttributeError: Accessing a non-existent attribute
    my_list = [1, 2, 3]
    print(my_list.upper())

    # IOError: Trying to open a non-existent file
    with open("nonexistent_file.txt", "r") as file:
        contents = file.read()

    # ZeroDivisionError: Dividing a number by zero
    result = 10 / 0

    # # ImportError: Importing a non-existent module
    # import non_existent_module
except SyntaxError as e:
    print("SyntaxError:", str(e))
except TypeError as e:
    print("TypeError:", str(e))
except NameError as e:
    print("NameError:", str(e))
except IndexError as e:
    print("IndexError:", str(e))
except KeyError as e:
    print("KeyError:", str(e))
except ValueError as e:
    print("ValueError:", str(e))
except AttributeError as e:
    print("AttributeError:", str(e))
except IOError as e:
    print("IOError:", str(e))
except ZeroDivisionError as e:
    print("ZeroDivisionError:", str(e))
except ImportError as e:
    print("ImportError:", str(e))
except Exception as e:
    print("An error occurred:", str(e))

# Here's a basic example that demonstrates
# the usage of try, except, else, and finally blocks:

try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
else:
    print("Division successful.")
finally:
    print("This code is always executed, regardless of exceptions.")


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message


try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise MyCustomException("Age cannot be negative.")
    else:
        print("Your age is:", age)
except MyCustomException as e:
    print("Custom Exception:", e.message)


# Implementing all the functions in File Handling

import os


def create_file(filename):
    try:
        with open(filename, "w") as file:
            file.write("Hello, world!\n")
        print(f"File {filename} created successfully.")
    except IOError as e:
        print(f"Error: could not create file {filename}. {str(e)}")


def read_file(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print(contents)
    except IOError as e:
        print(f"Error: could not read file {filename}. {str(e)}")


def append_file(filename, text):
    try:
        with open(filename, "a") as file:
            file.write(text)
        print(f"Text appended to file {filename} successfully.")
    except IOError as e:
        print(f"Error: could not append to file {filename}. {str(e)}")


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print(f"File {filename} renamed to {new_filename} successfully.")
    except IOError as e:
        print(f"Error: could not rename file {filename}. {str(e)}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted successfully.")
    except IOError as e:
        print(f"Error: could not delete file {filename}. {str(e)}")


if __name__ == "__main__":
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
