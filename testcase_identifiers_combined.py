import numpy as numpy_array13  # Import alias at the top

class MyClassName13:
    def __init__(self):
        self.attribute__13 = 'value'  # Attribute with length 13

    def function_13ch(self):
        _arg_with_13c = 42  # Argument with length 13
        return _arg_with_13c

def another_function():
    global global_var_13
    global_var_13 = 100  # Global variable with length 13

    def inner_function():
        nonlocal nonlocal_v_13
        nonlocal_v_13 = 200  # Nonlocal variable with length 13
        return nonlocal_v_13

    nonlocal_v_13 = 150  # Initialize nonlocal variable
    result = inner_function()  # Call inner function
    return result

if __name__ == "__main__":
    my_instance = MyClassName13()
    print(another_function())  # Should print 200
    print(my_instance.attribute__13)  # Accessing the class attribute
    #usage of numpy_array_13
    zeros_array = numpy_array13.zeros(3)
    print(zeros_array)  # Print an array of zeros
