# True Negative Test Case 2: Nested While and Try
def example_two():
    while True:  # Level 1
        try:  # Level 2
            x = int(input("Enter a number (0 to exit): "))  # Level 2
            if x == 0:  # Level 3
                break  # Level 4
        except ValueError:  # Level 2
            print("That's not a valid number!")  # Level 2

example_two()
