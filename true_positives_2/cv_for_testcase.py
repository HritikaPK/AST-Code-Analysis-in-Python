def test_for():
    for i in range(2):  # Depth 1
        for j in range(2):  # Depth 2
            for k in range(2):
                if j > 1:  # Depth 3
                    if m>10:
                        k=10  # Depth 4 (within limit)
                else:
                    l=2()  # Depth 2 (within limit)
        m=10  # Depth 1 (within limit)

test_for()
