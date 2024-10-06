def nested_except_handler():
    try:
        print("Outer try block 1")
        try:
            print("Outer try block 2")
            try:
                print("Outer try block 3")
                try:
                    print("Outer try block 4")
                    try:
                        print("Outer try block 5")
                        try:
                            print("Outer try block 6")
                            try:
                                print("Outer try block 7")
                                try:
                                    print("Outer try block 8")
                                    try:
                                        print("Outer try block 9")
                                        try:
                                            print("Outer try block 10")
                                            raise ValueError("An error occurred in block 10")
                                        except ValueError as e:
                                            print(f"Caught ValueError in block 10: {e}")
                                            if True:  # Condition to demonstrate nesting
                                                raise RuntimeError("Error in block 10")  # Nesting another error
                                        finally:
                                            print("Finally block 10 executed")
                                    except RuntimeError as e:
                                        print(f"Caught RuntimeError in block 9: {e}")
                                    finally:
                                        print("Finally block 9 executed")
                                except Exception as e:
                                    print(f"Caught Exception in block 8: {e}")
                                finally:
                                    print("Finally block 8 executed")
                            except Exception as e:
                                print(f"Caught Exception in block 7: {e}")
                            finally:
                                print("Finally block 7 executed")
                        except Exception as e:
                            print(f"Caught Exception in block 6: {e}")
                        finally:
                            print("Finally block 6 executed")
                    except Exception as e:
                        print(f"Caught Exception in block 5: {e}")
                    finally:
                        print("Finally block 5 executed")
                except Exception as e:
                    print(f"Caught Exception in block 4: {e}")
                finally:
                    print("Finally block 4 executed")
            except Exception as e:
                print(f"Caught Exception in block 3: {e}")
            finally:
                print("Finally block 3 executed")
        except Exception as e:
            print(f"Caught Exception in block 2: {e}")
        finally:
            print("Finally block 2 executed")
    except Exception as e:
        print(f"Caught Exception in block 1: {e}")
    finally:
        print("Finally block 1 executed")

# Call the test function
nested_except_handler()
