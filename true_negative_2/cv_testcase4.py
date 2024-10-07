# True Negative Test Case 4: Match and Multiple Ifs
def example_four(value):
    match value:  # Level 1
        case 1:  # Level 2
            print("One")  # Level 2
        case 2:  # Level 2
            print("Two")  # Level 2
        case _:  # Level 2
            print("Other")  # Level 2

example_four(2)
