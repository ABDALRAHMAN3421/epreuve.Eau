def two_nembers():
    for a in range (100):
        for b in range(a+ 1, 100):
            print(f"{format_number(a)} {format_number(b)},",end=" ")


def format_number(number):
    return f"{number:02}"


two_nembers()

