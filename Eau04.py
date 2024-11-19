import sys


if len(sys.argv) != 2: 
    print("Erreur : un seul argument est requis.")
    sys.exit(1)

argument = sys.argv[1]


if not argument.isdigit() or int(argument) < 0:
    print("Erreur : l'argument doit être un nombre entier positif.")
    sys.exit(1)

argument = int(argument)

def is_prime(num):
    if num <= 1:  
        return False
    for i in range(2, num):
        if num % i == 0:  
            return False
    return True


next_number = argument + 1
while True:
    if is_prime(next_number):
        break
    next_number += 1

print(next_number)
