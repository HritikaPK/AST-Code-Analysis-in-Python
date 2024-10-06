def nested_continue():
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
                            for o in range(1):
                                print("Outer loop 7")
                                for p in range(1):
                                    print("Outer loop 8")
                                    for q in range(1):
                                        print("Outer loop 9")
                                        for r in range(1):
                                            print("Outer loop 10")
                                            if r == 0:
                                                print("Continuing in loop 10")
                                                continue  # Continue in loop 10
                                            print("This won't be printed in loop 10")  # Won't be reached
                                        print("After loop 9")
                                        if q == 0:
                                            print("Continuing in loop 9")
                                            continue  # Continue in loop 9
                                    print("After loop 8")
                                    if p == 0:
                                        print("Continuing in loop 8")
                                        continue  # Continue in loop 8
                                print("After loop 7")
                                if o == 0:
                                    print("Continuing in loop 7")
                                    continue  # Continue in loop 7
                            print("After loop 6")
                            if n == 0:
                                print("Continuing in loop 6")
                                continue  # Continue in loop 6
                        print("After loop 5")
                        if m == 0:
                            print("Continuing in loop 5")
                            continue  # Continue in loop 5
                    print("After loop 4")
                    if l == 0:
                        print("Continuing in loop 4")
                        continue  # Continue in loop 4
                print("After loop 3")
                if k == 0:
                    print("Continuing in loop 3")
                    continue  # Continue in loop 3
            print("After loop 2")
            if j == 0:
                print("Continuing in loop 2")
                continue  # Continue in loop 2
        print("After loop 1")
        if i == 0:
            print("Continuing in loop 1")
            continue  # Continue in loop 1

# Call the test function
nested_continue()
