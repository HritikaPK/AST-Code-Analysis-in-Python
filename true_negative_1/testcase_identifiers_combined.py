print("All identifiers combined testcase")
print("")

import numpy as numpy_short  # Import alias at the top

class MyClassNameIsVeryLong:
    def __init__(self):
        self.short_attr = 'value'  

    def func_short(self):
        short_arg = 42  
        return short_arg

def another_function():
    global long_global_variable_name
    long_global_variable_name = 100  

    def inner_function():
        nonlocal nonlocal_v
        nonlocal_v = 200  
        return nonlocal_v

    nonlocal_v = 150  
    result = inner_function() 
    return result

if __name__ == "__main__":
    my_instance = MyClassNameIsVeryLong()
    print(another_function())  # Should print 200
    print(my_instance.short_attr)  
    
    zeros_array = numpy_short.zeros(3)
    print(zeros_array)  # Print an array of zeros
