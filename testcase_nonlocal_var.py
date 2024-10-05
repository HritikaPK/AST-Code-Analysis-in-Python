def outer_function():
    nonlocal_var_ = 30  # This nonlocal variable has 13 characters

    def inner_function():
        return nonlocal_var_
