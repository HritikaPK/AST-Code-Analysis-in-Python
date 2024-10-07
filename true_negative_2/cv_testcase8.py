# A bit complicated testcase

def example_function():
    # Level 1: If statement
    if True:
        print("This is level 1.")

        # Level 2: For loop
        for i in range(3):
            print("Looping through:", i)

            # Level 3: While loop
            while i < 2:
                print("Inside while loop with i:", i)
                i += 1  # Modify i to avoid infinite loop
            
            # Level 2 (still inside For): Try block
            try:
                print("Trying something...")
            except Exception as e:
                print("Caught an exception:", e)
            finally:
                print("Finished try-except.")

    # Level 1: Match statement
    match 1:
        case 1:
            print("Matched case 1")
            # Level 2: With statement
            with open("file.txt", "w") as f:
                f.write("Writing to file...")
        
        case 2:
            print("Matched case 2")
        
        case _:
            print("No match found.")

    # Level 1: Another Try block
    try:
        print("Executing another try block...")
    except Exception as e:
        print("Error occurred:", e)

# Call the function to run the test case
example_function()
