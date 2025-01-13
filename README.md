# AST Code Analysis in Python



## High Level Description

I have implemented the 2 analyses using the AST libraries built-in functions and classes.
This code is something I wrote to check for identifiers in Python code that have exactly 13 characters. I used Python's `ast` module to analyze the abstract syntax tree (AST) of the code. Here's how it works:

### Analysis 1: Identifier
This code utilizes Python's `ast` module to analyze Python scripts for identifiers that are exactly 13 characters long. I created a class called `IdentifierCheck`, which inherits from `ast.NodeVisitor`. In the initializer, I set up a set called `length_equals_13` to store unique identifiers meeting the length requirement.
The method `identifier_length_check()` checks if a name is a string and has a length of 13, adding it to the set if it does. To inspect different identifier types, I implemented several visitor methods. The `visit_Name()` method processes variable names, calling `identifier_length_check()` on `node.id`. The `visit_FunctionDef()` method handles function definitions, checking both the function name and its arguments. Similarly, the `visit_ClassDef()` method processes class names, while `visit_Attribute()` checks attribute names.
I also implemented `visit_Global()` and `visit_Nonlocal()` methods for global and nonlocal variable names, iterating through the names to apply the identifier check. The `visit_alias()` method verifies alias names, checking both `node.asname` and `node.name`.
The `display()` method outputs the results, showing found identifiers or indicating none were found. In the main block, the script expects a filename as input, reading the specified test case file. It uses `ast.parse()` to convert the code into an AST, and an instance of `IdentifierCheck` visits the parsed code. Finally, the `display()` method outputs the findings, with error handling for file-related issues.

### Analysis 2: Control Structure

This code uses Python's ast module to analyze the control flow depth of a Python script, focusing on how deeply control structures like if, for, and while are nested. I created a class called ControlFlowDepthAnalyzer, which extends ast.NodeVisitor to enable efficient traversal of the abstract syntax tree (AST) and inspection of its structure.
In the initializer, I defined current_depth to track the current nesting level and max_depth to store the deepest level encountered. A list called nested_blocks is also initialized, though it primarily serves as a placeholder for potentially tracking the names of control blocks.
The visit() function examines each node in the AST. When a node represents a control structure—such as ast.If, ast.For, ast.While, ast.With, ast.Try, ast.Match, ast.Break, ast.Continue—the code increases current_depth and checks if this is the deepest level seen so far by updating max_depth accordingly. I utilize self.generic_visit(node) to continue visiting child nodes, and after fully processing the current node, current_depth is decreased to reflect leaving the block.
Additionally, the report_depth() method prints whether the nesting depth is within a set limit (default is 4) or if it exceeds the allowed depth, ensuring that the code doesn’t become too complex regarding control flow.
In the main function, I open a test case file, convert it to an AST using ast.parse(), and pass it to the ControlFlowDepthAnalyzer for analysis. If the file doesn’t exist, the code handles this with a FileNotFoundError exception. By leveraging the built-in functionality of the ast module, the code efficiently analyzes the structure of scripts and identifies potential issues with control flow depth.

## Observations About False Negatives and False Positives:
### Dynamic Variable Names (false negative for Analysis 1):
In this test case, we create variable names dynamically using a dictionary instead of defining them directly in the code. While the AST can analyze static code, it cannot capture these dynamically generated identifiers like dynamic_var_0, dynamic_var_1, etc., since they are not explicitly defined in the source code.
As a result, if a static analysis tool checks for identifiers of length 13, it will find none, leading to a false negative.
### False Positive for Analysis 2: ast.ExceptHandler:
In the AST, the except Exception as e: clause would be represented by an ast.ExceptHandler node if ast.ExceptHandler is included in the code. Due to this, the nesting level would be calculated as one value greater which would be incorrect. Hence, I have omitted it in the true negative test cases. Otherwise, we would be getting a false positive.
