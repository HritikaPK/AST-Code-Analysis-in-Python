# True Negative Test Case 4: Match and Multiple Ifs
def example_four(value):
    match value:  # Level 1
        case 1:  
            print("One")  
        case 2:  
            print("Two")  
        case _:  
            print("Other")  

example_four(2)
