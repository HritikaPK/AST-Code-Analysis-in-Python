import ast
import sys

class ControlFlowDepthAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.current_depth = 0
        self.max_depth = 0
        self.nested_blocks = []  # Track names of control blocks

    def visit(self, node):
        """Override the visit method to track depth before calling the specific visit method."""
        # Check if the node is a control structure
        control_structures = (
            ast.If, ast.For, ast.While, ast.With, ast.Try, 
            ast.Match, ast.Break, ast.Continue,
            ast.ExceptHandler
        )

        if isinstance(node, control_structures):
            self.current_depth += 1
            self.max_depth = max(self.max_depth, self.current_depth)

        # Visit the node
        self.generic_visit(node)

        # Check for exit conditions and clean up
        if isinstance(node, control_structures):
            self.current_depth -= 1

    def report_depth(self, limit=4):
        """Generate a report based on the depth of nesting."""
        if self.max_depth > limit:
            print(f"Exceeded allowed nesting depth: {self.max_depth}")
        else:
            print(f"Nesting depth is within limit: {self.max_depth}")

# Main function to load test case files
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python control_flow_depth.py <test_case_filename>")
        sys.exit(1)

    test_case_file = sys.argv[1]

    try:
        # Open and read the test case file
        with open(test_case_file, 'r') as f:
            test_case_code = f.read()

        # Parse the test case into an AST
        parsed_code = ast.parse(test_case_code)

        # Initialize the analyzer and visit the parsed AST
        depth_analyzer = ControlFlowDepthAnalyzer()
        depth_analyzer.visit(parsed_code)

        # Output the results
        depth_analyzer.report_depth()

    except FileNotFoundError:
        print(f"Error: The file '{test_case_file}' was not found.")
