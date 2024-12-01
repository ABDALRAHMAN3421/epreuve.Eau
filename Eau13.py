import sys


def my_select_sort(array):
    n = len(array)
    sorted_array = array[:]  
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_array[j] < sorted_array[min_index]:
                min_index = j
        if min_index != i:
            temp = sorted_array[i]
            sorted_array[i] = sorted_array[min_index]
            sorted_array[min_index] = temp
    return sorted_array


def validate_numbers(arguments):
    validated_numbers = []
    for arg in arguments:
        
        if arg.replace('.', '', 1).isdigit() or (arg[0] == '-' and arg[1:].replace('.', '', 1).isdigit()):
            validated_numbers.append(float(arg))
        else:
            print(f"Erreur : '{arg}' n'est pas un nombre valide.")
            sys.exit(1)  
    return validated_numbers


def resolve():
    arguments = sys.argv[1:]
    if not arguments:
        print("Erreur : Aucun argument fourni.")
        sys.exit(1)  
    
    
    numbers = validate_numbers(arguments)
    sorted_numbers = my_select_sort(numbers)
    
    
    print(" ".join(map(str, sorted_numbers)))


