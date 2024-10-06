def nested_breaks():
    for i in range(1):
        print("Outer loop 1")
        for j in range(1):
            print("Outer loop 2")
            for k in range(1):
                print("Outer loop 3")
                for l in range(1):
                    print("Outer loop 4")
                    for m in range(1):
                        print("Outer loop 5")
                        for n in range(1):
                            print("Outer loop 6")
                            if n == 0:
                                print("Breaking out of loop 6")
                                break  # Break from loop 6
                        print("After loop 5")
                        if m == 0:
                            print("Breaking out of loop 5")
                            break  # Break from loop 5
                    print("After loop 4")
                    if l == 0:
                        print("Breaking out of loop 4")
                        break  # Break from loop 4
                print("After loop 3")
                if k == 0:
                    print("Breaking out of loop 3")
                    break  # Break from loop 3
            print("After loop 2")
            if j == 0:
                print("Breaking out of loop 2")
                break  # Break from loop 2
        print("After loop 1")
        if i == 0:
            print("Breaking out of loop 1")
            break  # Break from loop 1

# Call the test function
nested_breaks()
