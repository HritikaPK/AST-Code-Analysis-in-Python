def handle_file_operations():
    try:
        with open('file1.txt') as f:
            data = f.read()
            if "error" in data:
                print("Error found in file1.")
            else:
                print("No issues in file1.")
                
            try:
                with open('file2.txt') as f2:
                    data2 = f2.read()
                    if "warning" in data2:
                        print("Warning found in file2.")
                    else:
                        print("No warnings in file2.")
                        
                    try:
                        with open('file3.txt') as f3:
                            data3 = f3.read()
                            if "critical" in data3:
                                print("Critical issue found in file3.")
                            else:
                                print("No critical issues in file3.")
                                
                            try:
                                with open('file4.txt') as f4:
                                    data4 = f4.read()
                                    if "failure" in data4:
                                        print("Failure detected in file4.")
                                    else:
                                        print("No failures in file4.")
                            except FileNotFoundError:
                                print("file4.txt not found.")
                    except FileNotFoundError:
                        print("file3.txt not found.")
            except FileNotFoundError:
                print("file2.txt not found.")
    except FileNotFoundError:
        print("file1.txt not found.")

handle_file_operations()
