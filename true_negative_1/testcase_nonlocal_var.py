def outer_function():
    nonlocal_variable_long = 30  # This nonlocal variable has 13 characters

    def inner_function():
        return nonlocal_variable_long
