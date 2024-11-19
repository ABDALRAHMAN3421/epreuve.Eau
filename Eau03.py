import sys

def fibonacci_with_elemnt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1


    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

def get_argument():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 0:
        print("Erreur : l'argument doit être un nombre entier positif")
        sys.exit(1)
    return int(sys.argv[1])


argument = get_argument()
result = fibonacci_with_elemnt(argument)

print(result)
