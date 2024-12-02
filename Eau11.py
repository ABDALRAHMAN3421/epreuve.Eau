def minimal_difference(arg):
    arg = sorted(arg)
    min_difference = float('inf')

    
    for i in range(len(arg) - 1):
        current_difference = abs(arg[i] - arg[i + 1])
        if current_difference < min_difference:
            min_difference = current_difference

    return min_difference

def is_a_number(arg):
    for item in arg:
        if item.lstrip('-').replace('.', '', 1).isdigit() == False:
            return False
    return True

def get_argument():
    import sys
    return sys.argv[1:]  

my_argument = get_argument()

if is_a_number(my_argument):
    my_argument = [float(x) for x in my_argument]
    result = minimal_difference(my_argument)
    print(result)
else:
    print("Erreur : L'argument doit être un nombre.")

