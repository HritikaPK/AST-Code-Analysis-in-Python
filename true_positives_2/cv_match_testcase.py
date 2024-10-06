def match_test(value):
    match value:
        case 1:
            print("Matched case 1")
            match value % 2:
                case 0:
                    print("1 is even")
                case 1:
                    print("1 is odd")
        case 2:
            print("Matched case 2")
            match value // 2:
                case 1:
                    print("Half of 2 is 1")
                    match value % 2:
                        case 0:
                            print("2 is even")
                            match value // 2:
                                case 1:
                                    print("Even case checks out.")
                        case 1:
                            print("2 is odd")
        case 3:
            print("Matched case 3")
            match value:
                case 3 | 5 | 7:
                    print("Matched an odd number: 3, 5, or 7")
                    match value:
                        case 3:
                            print("Special case for 3")
                            match value * 2:
                                case 6:
                                    print("Double of 3 is 6")
                                    if value > 0:
                                        print("3 is positive")
                                        if value < 5:
                                            print("3 is less than 5")
                                    else:
                                        print("3 is not positive")
                        case 5:
                            print("Matched 5")
                        case 7:
                            print("Matched 7")
        case _:
            print("No match found for the value")
            match value:
                case 4 | 8:
                    print("Matched a special case for even numbers 4 or 8")
                    match value // 2:
                        case 2:
                            print("Half of 4 is 2")
                            if value == 4:
                                print("Confirmed it is 4")
                        case 4:
                            print("Half of 8 is 4")
                            if value == 8:
                                print("Confirmed it is 8")
                case _:
                    print("Just a regular unmatched number")

# Test the function with various values
match_test(1)
match_test(2)
match_test(3)
match_test(4)
match_test(5)
match_test(8)
