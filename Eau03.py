import sys

def fibonacci_nth_element(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def is_number(argument):
    if not isinstance(argument, int) or argument < 0:
        print("Erreur : l'argument doit être un nombre entier positif")
        sys.exit(1)



def get_argument():
    if len(sys.argv) < 2:
        print("Erreur : veuillez fournir un argument")
        sys.exit(1)
    try:
        argument = int(sys.argv[1])
    except ValueError:
        print("Erreur : l'argument doit être un nombre entier")
        sys.exit(1)
    return argument


argument = get_argument()
is_number(argument)

result = fibonacci_nth_element(argument)


print(result)
