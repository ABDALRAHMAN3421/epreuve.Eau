def get_age():
    while True:
        age, success = try_get_age()
        if success:
            print("True")
            break
        else:
            print("False")

def try_get_age():
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        return int(user_input), True
    else:
        return None, False

get_age()
