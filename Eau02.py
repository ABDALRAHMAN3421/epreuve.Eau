import sys

def validate_arguments(arguments):
    if len(arguments) < 2:
        print("Error: Please provide at least two arguments.")
        sys.exit(1)

def print_arguments_in_reverse(arguments):
    for i in range(len(arguments) - 1, -1, -1):
        print(arguments[i])

def main():
    arguments = sys.argv[1:]
    

    reverse_list = False
    if '--reverse' in arguments:
        reverse_list = True
        arguments.remove('--reverse')  
    

    validate_arguments(arguments)
    

    if reverse_list:
        print_arguments_in_reverse(arguments)
    else:
        for argument in arguments:
            print(argument)

