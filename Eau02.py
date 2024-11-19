import sys

def reverse_argument():
    argument = sys.argv[1:]

    result = ""
    for i in range(len(argument) - 1, -1, -1):
        result += argument[i]
        if i > 0:
            result += ' '


    print(result)

reverse_argument()
