print("non-local variable name testcase")
print("")
def outer_function():
    nonlocal_variable_long = 30  

    def inner_function():
        return nonlocal_variable_long
