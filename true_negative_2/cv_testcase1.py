# True Negative Test Case 1: Simple If and For Loop Nesting
def example_one():
    for i in range(3):  # Level 1
        if i > 1:  # Level 2
            print(i)  # Level 2
        else:  # Level 2
            print("Less than or equal to 1")  # Level 2

example_one()
