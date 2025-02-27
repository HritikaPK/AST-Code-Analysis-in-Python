import ast
import sys

class IdentifierCheck(ast.NodeVisitor):
    def __init__(self):
        # Set to store unique identifiers of length 13
        self.length_equals_13 = set()

    # Check if name is string and identifier length is 13
    def identifier_length_check(self, name):
        if isinstance(name, str) and len(name) == 13:
            self.length_equals_13.add(name)  # Use add() for sets

    # Variable names
    def visit_Name(self, node):
        self.identifier_length_check(node.id)
        self.generic_visit(node)
    
    # Function names and argument names
    def visit_FunctionDef(self, node):
        self.identifier_length_check(node.name)
        for arg in node.args.args:
            self.identifier_length_check(arg.arg)
        self.generic_visit(node)

    # Class names
    def visit_ClassDef(self, node):
        self.identifier_length_check(node.name)
        self.generic_visit(node)

    # Attribute names
    def visit_Attribute(self, node):
        self.identifier_length_check(node.attr)
        self.generic_visit(node)
    
    # Global variable names
    def visit_Global(self, node):
        for name in node.names:
            self.identifier_length_check(name)
        self.generic_visit(node)
    
    # Nonlocal variable names
    def visit_Nonlocal(self, node):
        for name in node.names:
            self.identifier_length_check(name)
        self.generic_visit(node)

    # Alias names
    def visit_alias(self, node):
        self.identifier_length_check(node.asname)
        self.identifier_length_check(node.name)
        self.generic_visit(node)

    # Display result
    def display(self):
        if self.length_equals_13:
            print("Identifiers with length 13:", list(self.length_equals_13))
        else:
            print("No identifiers with length 13 were found.")

# load test case files
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python identifiers.py <test_case_filename>")
        sys.exit(1)

    test_case_file = sys.argv[1]

    try:
        # Open and read testcase file
        with open(test_case_file, 'r') as f:
            test_case_code = f.read()

        # Parse the test case into an AST
        parsed_code = ast.parse(test_case_code)

        # Initialize 
        identifier_checker = IdentifierCheck()
        identifier_checker.visit(parsed_code)

        # Output 
        identifier_checker.display()

    except FileNotFoundError:
        print(f"Error: The file '{test_case_file}' was not found.")
