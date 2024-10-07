# True Negative Test Case 6: Nested If and Try
def example_six():
    try:  # Level 1
        value = 10  # Level 2
        if value > 5:  # Level 2
            print("Greater than 5")  # Level 2
    except Exception as e:  # Level 1
        print("An error occurred")  # Level 1

example_six()
