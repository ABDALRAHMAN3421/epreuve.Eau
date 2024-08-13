import sys

def my_select_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def process_input(user_input):
    try:
        numbers = [int(i) for i in user_input.split()]
        return numbers
    except ValueError:
        return None

def main():
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:])
    else:
        user_input = input("Entrez vos nombres séparés par des espaces : ")
    
    numbers = process_input(user_input)
    
    if numbers is not None:
        sorted_numbers = my_select_sort(numbers)
        print("Tableau trié :", sorted_numbers)
    else:
        print("Erreur : veuillez entrer des nombres valides.")

    main()
