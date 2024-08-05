import sys

def fibonacci(i):
    if i == 0:
        return 0 
    elif i == 1:
        return i
    else:
        return fibonacci(i-2) + fibonacci(i-1)

def get_input():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Enter a number: ")

def validate_input(n):
    if not n.isdigit():
        print("error")
        return False
    elif int(n) <= 0:
        print("you can't enter a value that goes from 0 and down")
        return False
    return True

def main():
    n = get_input()
    if validate_input(n):
        n = int(n)
        print(fibonacci(n))
        return True
    return False

success = main()
print("Execution was successful:", success)
