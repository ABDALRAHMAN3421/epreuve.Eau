import sys


def is_slice(argument, argument2):
    i = 0
    j = 0

    while i < len(argument):
        j = i + 1
        while j <= len(argument):
            match = True
            if len(argument[i:j]) == len(argument2):
                for k in range(len(argument2)):
                    if argument[i + k] != argument2[k]:
                        match = False
                        break
                if match:
                    return {"i": i, "j": j}
            j += 1
        i += 1

    return {"i": -1, "j": -1}

def verify_slice(argument1, argument2):
    result = is_slice(argument1, argument2)
    i, j = result["i"], result["j"]
    if i != -1 and j != -1:
        print("true")
    else:
        print("false")


def main():
    if len(sys.argv) != 3:
        print("Error: Veuillez fournir deux chaînes de caractères en arguments.")
        sys.exit(1)

   
    argument1 = sys.argv[1]
    argument2 = sys.argv[2]

    
    if not argument1.isalpha() or not argument2.isalpha():
        print("Error: Les arguments doivent être des chaînes de caractères contenant uniquement des lettres.")
        sys.exit(1)

 
    verify_slice(argument1, argument2)


main()
