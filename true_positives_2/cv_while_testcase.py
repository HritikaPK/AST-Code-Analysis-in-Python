def count_numbers(num_list):
    total_count = 0
    index = 0
    length = len(num_list)

    while index < length:
        number = num_list[index]
        count = 0

        while count < number:
            count += 1

            while count < 5:
                count += 1

                while count < 10:
                    count += 1

                    while count < 12:
                        count += 1

                        if count == 11:
                            print(f"Count reached 11 at index {index}.")

                            if count % 2 == 0:
                                print(f"Count {count} is even at index {index}. Incrementing by 1.")
                                count += 1  # Increment to make it odd
                                print(f"Count after incrementing is now: {count}.")

                                if count == 12:
                                    print(f"Count reached 12 at index {index}. Ending this loop.")
                        else:
                            if count % 2 != 0:
                                print(f"Count {count} is odd at index {index}. Incrementing by 1.")
                                count += 1  # Increment to make it even
                                print(f"Count after incrementing is now: {count}.")

                    while count < 15:
                        count += 1

        total_count += count
        index += 1

    print(f"Total count of numbers processed: {total_count}")

numbers = [3, 5, 2, 7]
count_numbers(numbers)
