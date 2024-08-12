import sys

def bubble_sort(a):
    numbers = len(a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, numbers):
            if a[i] > a[i+1]:
                sorted = False
                a[i], a[i+1] = a[i+1], a[i]
    return a

def process_input(user_input):
    try:
        a = list(map(int, user_input.split()))
        return a
    except ValueError:
        return None

def main():
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:])
    else:
        user_input = input("Entrez vos nombres : ")
    
    a = process_input(user_input)
    
    if a is not None:
        sorted_a = bubble_sort(a)
        print("Tableau trié :", sorted_a)
    else:
        print("Erreur : veuillez entrer des nombres valides.")


    main()
