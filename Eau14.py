import sys


def get_arguments():
    arguments = sys.argv[1:]  
    if not arguments:
        print("Error: No arguments provided.")
        sys.exit(1)  
    return arguments


def sort_ascii(arguments):
    for i in range(len(arguments) - 1):
        for j in range(len(arguments) - i - 1):
            if list(map(ord, arguments[j])) > list(map(ord, arguments[j + 1])):
                arguments[j], arguments[j + 1] = arguments[j + 1], arguments[j]
    return arguments


arguments = get_arguments()
sorted_arguments = sort_ascii(arguments)
result = " ".join(sorted_arguments)


print(result)

