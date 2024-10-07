import ast
import sys

class MaxControlStruct(ast.NodeVisitor):
    def __init__(self):
        self.present_depth = 0
        self.maximum = 0
        self.nested = []  

    def visit(self, node):
        cs = (ast.If, ast.For, ast.While, ast.With, ast.Try, ast.Match, ast.Break, ast.Continue,ast.ExceptHandler)

        if isinstance(node, cs):
            self.present_depth += 1
            self.maximum = max(self.maximum, self.present_depth)

        self.generic_visit(node)

        if isinstance(node, cs):
            self.present_depth -= 1

    def display(self, limit=4):
        if self.maximum > limit:
            print(f"Exceeded allowed nesting depth: {self.maximum}")
        else:
            print(f"Nesting depth is within limit: {self.maximum}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python control_flow_depth.py <testcasename>")
        sys.exit(1)

    testcase = sys.argv[1]
    try:
        
        with open(testcase, 'r') as f:
            test_case_code = f.read()
        
        parsed_code = ast.parse(test_case_code)
        
        depth_analyzer = MaxControlStruct()
        depth_analyzer.visit(parsed_code)

        
        depth_analyzer.display()

    except FileNotFoundError:
        print(f"Error: The file '{testcase}' was not found.")
