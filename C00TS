import os
import re

# Prompt the user to choose a mode
mode = raw_input("Enter 'auto' for automatic mode or 'manual' for manual mode: ")

# Prompt the user to choose a folder
folder = raw_input("Enter the path of the folder to process: ")

if mode == "auto":
    # Find all subdirectories in the specified folder
    subdirs = [os.path.join(folder, d) for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]

    # Process each subdirectory
    for subdir in subdirs:
        # Find all C files in the current subdirectory
        c_files = [os.path.join(subdir, f) for f in os.listdir(subdir) if f.endswith(".c")]

        # Skip this subdirectory if it contains no C files
        if not c_files:
            continue

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

        # Create the main.c file in the current subdirectory
        with open(os.path.join(subdir, "main.c"), "w") as f:
            # Write include statements for unistd.h and stdio.h
            f.write('#include <unistd.h>\n')
            f.write('#include <stdio.h>\n\n')

            # Write function prototypes for each function in the specified C file
            for func in functions:
                return_type, func_name, params = func
                f.write("{} {}({});\n".format(return_type, func_name, params))

            # Write the main function
            f.write("\nint main(void) {\n")
            for funcname in function_names:
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

                # Write a call to the specified function with appropriate arguments
                f.write("    // Call {} with appropriate arguments\n".format(funcname))
                f.write("    {}({});\n".format(funcname, ", ".join(args)))

            f.write("\n    return 0;\n")
            f.write("}\n")

        print("main.c created in {} with calls to all functions with appropriate arguments.".format(subdir))
elif mode == "manual":
    # Prompt the user to choose a subdirectory
    subdir = raw_input("Enter the path of the subdirectory to process: ")

    # Find all C files in the specified subdirectory
    c_files = [os.path.join(subdir, f) for f in os.listdir(subdir) if f.endswith(".c")]

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
    print("Functions found in C files in {}:".format(subdir))
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

    # Create the main.c file in the specified subdirectory
    with open(os.path.join(subdir, "main.c"), "w") as f:
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

    print("main.c created in {} with a call to {} with appropriate arguments.".format(subdir, funcname))
else:
    print("Invalid mode entered. Please enter 'auto' or 'manual'.")

