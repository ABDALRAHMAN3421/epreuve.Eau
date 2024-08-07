import sys

def search_chain(chain_principal, chain_search): 
    if chain_search in chain_principal: 
        return True  
    else:
        return False  

def get_user_input(prompt):
    user_input = input(prompt)
    if user_input:
        return user_input
    else:
        print(f"Invalid input for {prompt.strip(': ')}", file=sys.stderr)
        return None

def main():
    chain_principal = get_user_input("Entrée la chaîne principale : ") 
    chain_search = get_user_input("Entrée la chaîne à rechercher : ") 

    if chain_principal is None or chain_search is None:
        print("Error in input. Exiting.")
        return

    if search_chain(chain_principal, chain_search): 
        print("La chaîne recherchée est présente dans la chaîne principale.") 
    else:
        print("La chaîne recherchée n'est pas présente dans la chaîne principale.")


main()