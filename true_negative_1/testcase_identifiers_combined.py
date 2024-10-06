import numpy as numpy_short  # Import alias at the top

class MyClassNameIsVeryLong:
    def __init__(self):
        self.short_attr = 'value'  # Attribute with length 13

    def func_short(self):
        short_arg = 42  # Argument with length 13
        return short_arg

def another_function():
    global long_global_variable_name
    long_global_variable_name = 100  # Global variable with length 13

    def inner_function():
        nonlocal nonlocal_v
        nonlocal_v = 200  # Nonlocal variable with length 13
        return nonlocal_v

    nonlocal_v = 150  # Initialize nonlocal variable
    result = inner_function()  # Call inner function
    return result

if __name__ == "__main__":
    my_instance = MyClassNameIsVeryLong()
    print(another_function())  # Should print 200
    print(my_instance.short_attr)  # Accessing the class attribute
    #usage of numpy_array_13
    zeros_array = numpy_short.zeros(3)
    print(zeros_array)  # Print an array of zeros
