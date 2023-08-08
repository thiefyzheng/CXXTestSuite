import os
import re

# Find all C files in the current working directory
c_files = [f for f in os.listdir(os.getcwd()) if f.endswith(".c")]

# Create a list to store the names of all functions in all C files
function_names = []

# Process each C file
for c_file in c_files:
    # Open the C file and read its contents
    with open(c_file, "r") as f:
        c_code = f.read()

    # Use a regular expression to find all function declarations in the C code
    function_regex = r"(\w+)\s+(\w+)\s*\(([^)]*)\)"
    functions = re.findall(function_regex, c_code)

    # Add the names of all functions in this C file to the list
    for func in functions:
        return_type, func_name, params = func
        function_names.append(func_name)

# Print a numbered list of all function names
print("Functions found in C files:")
for i, func_name in enumerate(function_names):
    print("{}. {}".format(i + 1, func_name))

# Prompt the user to choose a function to test by entering its number
func_index = int(raw_input("Enter the number of the function to test: ")) - 1
funcname = function_names[func_index]

# Find the C file containing the specified function
c_file = ""
for f in c_files:
    with open(f, "r") as file:
        if funcname in file.read():
            c_file = f
            break

# Open the C file and read its contents
with open(c_file, "r") as f:
    c_code = f.read()

# Use a regular expression to find all function declarations in the C code
function_regex = r"(\w+)\s+(\w+)\s*\(([^)]*)\)"
functions = re.findall(function_regex, c_code)

# Find the specified function and extract its parameter list
params = ""
for func in functions:
    return_type, func_name, param_list = func
    if func_name == funcname:
        params = param_list
        break

# Split the parameter list into individual parameters
params = [p.strip() for p in params.split(",")]

# Create a list of arguments to pass to the function
args = []
for param in params:
    # Handle functions with void parameter lists
    if param == "void":
        continue

    # Extract the parameter type and name
    param_type, param_name = param.split()
    # Choose an appropriate argument value based on the parameter type
    if param_type == "int":
        arg_value = "42"
    elif param_type == "char":
        arg_value = "'A'"
    elif param_type == "float" or param_type == "double":
        arg_value = "3.14"
    else:
        arg_value = "0"
    args.append(arg_value)

# Create the main.c file
with open("main.c", "w") as f:
    # Write include statements for unistd.h and stdio.h
    f.write('#include <unistd.h>\n')
    f.write('#include <stdio.h>\n\n')

    # Write function prototypes for each function in the specified C file
    for func in functions:
        return_type, func_name, params = func
        f.write("{} {}({});\n".format(return_type, func_name, params))

    # Write the main function
    f.write("\nint main(void) {\n")
    f.write("    // Call the specified function with appropriate arguments\n")
    f.write("    {}({});\n".format(funcname, ", ".join(args)))
    f.write("\n    return 0;\n")
    f.write("}\n")

print("main.c created with a call to {} with appropriate arguments.".format(funcname))
