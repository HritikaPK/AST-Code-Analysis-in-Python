# True Negative Test Case 5: For Loop with Break and Continue
def example_five():
    for i in range(5):  # Level 1
        if i % 2 == 0:  # Level 2
            continue  # Level 3
        print(i)  

example_five()
