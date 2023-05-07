import ast

# Read the input
input_data = input()

# Use ast.literal_eval to evaluate the input
try:
    evaluated_data = ast.literal_eval(input_data)
    data_type = type(evaluated_data).__name__
    
    if data_type == 'int':
        print('This input is of type Integer.')
    elif data_type == 'float':
        print('This input is of type Float.')
    elif data_type == 'str':
        print('This input is of type String.')
    else:
        print('This is something else.')
except (ValueError, SyntaxError):
    print('This is something else.')
