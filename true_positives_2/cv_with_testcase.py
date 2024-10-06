def process_files():
    with open('file1.txt') as f:
        data = f.read()
        if "error" in data:
            print("Error found in file1.")
            
            with open('file2.txt') as f2:
                data2 = f2.read()
                if "warning" in data2:
                    print("Warning found in file2.")

                    with open('file3.txt') as f3:
                        data3 = f3.read()
                        if "critical" in data3:
                            print("Critical issue found in file3.")
                            
                            with open('file4.txt') as f4:
                                data4 = f4.read()
                                if "failure" in data4:
                                    print("Failure detected in file4.")
                                    
                                    with open('file5.txt') as f5:
                                        data5 = f5.read()
                                        if "success" in data5:
                                            print("Success detected in file5.")
                                            
                                            with open('file6.txt') as f6:
                                                data6 = f6.read()
                                                if "complete" in data6:
                                                    print("Process complete in file6.")

files_to_process = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt']
process_files()
