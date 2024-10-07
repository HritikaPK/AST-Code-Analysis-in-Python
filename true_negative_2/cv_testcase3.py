# True Negative Test Case 3: With Statement and If
def example_three():
    with open('file.txt', 'r') as f:  # Level 1
        if f.read():  # Level 2
            print("File is not empty")  # Level 2
        else:  # Level 2
            print("File is empty")  # Level 2

example_three()
