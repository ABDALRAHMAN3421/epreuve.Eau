import sys


user_inputs = sys.argv[1:]


if len(user_inputs) < 2:
    print("Error: Please provide at least two arguments.")
    sys.exit(1)  


reverse_list = True  


if reverse_list:
    reversed_inputs = []
    for i in range(len(user_inputs) - 1, -1, -1):
        reversed_inputs.append(user_inputs[i])
    user_inputs = reversed_inputs


for input_item in user_inputs:
    print(input_item)
