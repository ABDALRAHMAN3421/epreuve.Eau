import sys

def get_input():
    try:
        number = int(input("Please enter a number: "))
        return number, True
    except ValueError:
        return None, False

def validate_input(number):
    if number == 0 or number == -1:
        return False, "You can't enter a value that goes from 0 and down."
    return True, None

def calculate_next_odd(number):
    if number % 2 == 0:
        return number + 1
    else:
        return number + 2

def handle_error(message):
    print(message)
    sys.exit(1)

def display_result(number, next_odd):
    print(f"The next odd number after {number} is {next_odd}")

def main():
    number, valid_input = get_input()
    
    if not valid_input:
        handle_error("Invalid input. Please enter a valid number.")
    
    is_valid, error_message = validate_input(number)
    
    if not is_valid:
        handle_error(error_message)
    
    next_odd = calculate_next_odd(number)
    display_result(number, next_odd)
    return True


execution_success = main()
print("Execution was successful:", execution_success)
