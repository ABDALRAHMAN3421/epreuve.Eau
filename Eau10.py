import sys

def find_index(arg):
    result = -1
    last_word = arg[-1]
    for i in range(len(arg) - 1):
        if arg[i] == last_word:
            result = i
            break
    return result

def get_argument():
    if len(sys.argv) > 1:
        argument = sys.argv[1:]
        return argument
    else:
        print("Error: No arguments provided.")
        return []
        
my_argument = get_argument()

if my_argument:
    result = find_index(my_argument)
    print(result)
else:
    print("Error: No valid argument found.")
