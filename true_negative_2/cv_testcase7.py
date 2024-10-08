# True Negative Test Case 7: Combining Loops with Try
def example_seven():
    for i in range(3):  # Level 1
        try:  # Level 2
            if i < 2:  # Level 3
                print(f"Number: {i}")  # Level 2
        except Exception:  # Level 2
            print("An exception occurred")  # Level 2

example_seven()
