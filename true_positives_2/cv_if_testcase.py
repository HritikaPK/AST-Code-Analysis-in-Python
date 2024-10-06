def test_if():
    i = 1000
    if i >1:
        if i > 10:  # Depth 2
            if i > 100:  # Depth 3
                if i>200:  # Depth 4 
                    if i > 300:
                        i = 876
            else:
                i=24  # Depth 3 (within limit)
        else:
            i=999()  # Depth 2 (within limit)

# Call the test function
test_if()
