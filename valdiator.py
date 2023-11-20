import os

def validate_string_input(func):
    def inner(x):
        while True:
            try:
                value = input(x)
                if not isinstance(x, str):
                    raise ValueError("Enter a string.")
                if not value:
                    raise ValueError("This shouldn't be empty.")
                if not all(c.isalpha() or c.isspace() for c in value):
                    raise ValueError("Enter a valid string")
                return value
            except ValueError as e:
                print(f"{e}")
    return inner

def validate_int_input(func):
    def inner(x):
        while True:
            try:
                value = int(input(x))
                if value < 0:
                    raise ValueError("This number should be positive.")
                return value
            except ValueError as e:
                print(f"{e}")
    return inner  

def validate_file(func):
    def inner(x):
        while True:
            try:
                value = input(x)
                if not value:
                    raise ValueError("This shouldn't be empty.")
                if not os.path.isfile(value):
                    raise ValueError("This file doesn't exist.")
                return value
            except ValueError as e:
                print(f"{e}")
    return inner