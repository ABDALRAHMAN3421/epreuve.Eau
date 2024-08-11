import sys

def min_abs_difference(arr):
    arr.sort()  
    min_diff = float('infinity')  

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])  
        min_diff = min(min_diff, diff)  

    return min_diff

def main_logic():
    numbers_input = input("Please enter some numbers: ")

    if numbers_input:
        split_numbers = numbers_input.split()
        if all(num.lstrip('-').isdigit() for num in split_numbers):
            numbers = list(map(int, split_numbers))
            if len(numbers) > 1:
                result = min_abs_difference(numbers)
                print("Minimum absolute difference:", result)
            else:
                print("An error occurred: Please enter at least two numbers.")
        else:
            print("An error occurred: Please enter valid integers separated by spaces.")
    else:
        print("An error occurred: Input cannot be empty.")

main_logic()
