import sys

def is_string_of_number(arg):
    for char in arg:
        if not char.isdigit():
            return False
    return True

def number_of_argument_and_validity():
    if len(sys.argv) != 2:
        print("Erreur : Le programme prend un seul argument.")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("Erreur : L'argument ne doit contenir que des chiffres.")
        sys.exit(1)


def get_argument():
    return sys.argv[1]


number_of_argument_and_validity()
argument = get_argument()
print(is_string_of_number(argument))
