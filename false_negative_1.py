# Test case demonstrating dynamic variable creation

# Creating variable names dynamically using exec
dynamic_vars = {}
for i in range(5):
    dynamic_vars[f"dynamic_var_{i}"] = i

# Accessing the dynamically created variables
print(dynamic_vars["dynamic_var_0"])  # Should output: 0
print(dynamic_vars["dynamic_var_1"])  # Should output: 1
print(dynamic_vars["dynamic_var_2"])  # Should output: 2
print(dynamic_vars["dynamic_var_3"])  # Should output: 3
print(dynamic_vars["dynamic_var_4"])  # Should output: 4

