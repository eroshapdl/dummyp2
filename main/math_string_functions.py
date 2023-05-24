#math Functions
def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero"
    
def power_of_number(a, b):
    return a ** b

#string Functions


def concatenate_strings(a, b):
    return a + b


def capitalize_string(string):
    return string.capitalize()


def reverse_string(string):
    return string[::-1]



#math functions
print(add_numbers(2, 3))
print(subtract_numbers(8, 4))
print(multiply_numbers(7, 2))
print(divide_numbers(20, 10))
print(power_of_number(2, 3))

#string functions
print(concatenate_strings("Hello", "World"))
print(capitalize_string("hello"))
print(reverse_string("hello"))

