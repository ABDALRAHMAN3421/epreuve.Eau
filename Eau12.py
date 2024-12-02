def my_bubble_sort(array):
    sorted_array = array[:]
    n = len(sorted_array)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            sorted_array[j] = float(sorted_array[j])
            sorted_array[j + 1] = float(sorted_array[j + 1])

            if sorted_array[j] > sorted_array[j + 1]:
                temp = sorted_array[j]
                sorted_array[j] = sorted_array[j + 1]
                sorted_array[j + 1] = temp

    return sorted_array


def validate_numbers(array):
    for element in array:
        if not element.replace('.', '', 1).isdigit() or element.count('.') > 1:
            print("Erreur : Tous les éléments doivent être des nombres.")
            return False
    return True


def resolution():
    import sys
    arguments = sys.argv[1:]

    if not arguments or not validate_numbers(arguments):
        print("Programme terminé en raison d'une erreur d'entrée.")
        return
        
    sorted_result = my_bubble_sort(arguments)


    print(" ".join(map(str, sorted_result)))


