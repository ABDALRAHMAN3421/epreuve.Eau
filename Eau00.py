def show_three_numbers():
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                combine_numbers(a + b + c)
                


def combine_numbers(A, B, C):
    combination = [A, B, C]
    show_numbers(combination)
    


def show_numbers(combination):
    print(combination)

show_three_numbers()

