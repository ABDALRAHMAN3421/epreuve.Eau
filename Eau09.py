import sys

def valeurs_entre(minimum, maximum):
    if minimum >= maximum:
        print("Error: The minimum number must be less than the maximum number.")
        return

    for i in range(minimum, maximum):
        print(i, end=" ")

def get_min_max():
    min_val = input("Enter the minimum number: ")
    max_val = input("Enter the maximum number: ")
    
    if min_val.isdigit() and max_val.isdigit():
        return int(min_val), int(max_val), True
    else:
        return None, None, False

def main():
    while True:
        min_val, max_val, success = get_min_max()
        if success:
            valeurs_entre(min_val, max_val)
            break
        else:
            print("Error: Please enter valid numbers.")

print(main)
