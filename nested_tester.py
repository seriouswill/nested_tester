from random import random, randint

def check_answer(user_input, correct_answer):
    if user_input == correct_answer:
        return "Well done, that is correct."

def continue_playing():
    choice = input("Coninue? Y/N: ")
    if choice == "Y":
        pass
    else:
        exit()

def level_one():
    rand_num = randint(0, 9)
    rand_index = randint(0, 9)  # Random index for the list
    list_one = [i for i in range(rand_num, rand_num + 10)]
    print(f"This is the list for the first level: \n{list_one}")
    choice = input(f"Please write the syntax for retrieving the element at index {rand_index} in the list called 'list_one', which in this case is {list_one[rand_index]}:\n")
    if choice == "show":
        print(f"\nHere is the data structure again:\n{list_one}\n")
        level_one()
    elif choice == "skip":
        pass
    elif str(choice) == f"list_one[{rand_index}]":
        print("Well done, that is correct.")
        continue_playing()
    else:
        print("Incorrect. Please try again.")
        exit()


def level_two():
    keys = [f"key_{i}" for i in range(1, 6)]
    rand_key = random.choice(keys)  # Random key selection
    dict_one = {key: i for i, key in enumerate(keys, start=1)}
    print(f"\nThis is the dictionary for the second level: \n{dict_one}")
    choice = input(f"Please write the syntax for retrieving the value associated with '{rand_key}' in the dictionary called 'dict_one', which in this case is {dict_one[rand_key]}:\n")
    if choice == "show":
        print(f"\nHere is the data structure again:\n{dict_one}")
        level_two()
    elif choice == "skip":
        pass
    elif str(choice) == f"dict_one['{rand_key}']":
        print("Well done, that is correct.")
        continue_playing()
    else:
        print("Incorrect. Please try again.")
        exit()


def level_three():
    outer_index = randint(0, 2)  # Random index for the outer list
    inner_index = randint(0, 2)  # Random index for the inner list
    nested_list = [[i for i in range(j, j + 3)] for j in range(0, 9, 3)]
    print(f"\nThis is the nested list for the third level: {nested_list}")
    choice = input(f"Please write the syntax for retrieving the element at index {inner_index} of the list at index {outer_index} in the nested list called 'nested_list', which in this case is {nested_list[outer_index][inner_index]}:\n")
    if choice == "show":
        print(f"\nHere is the data structure again:\n{nested_list}")
        level_three()
    elif choice == "skip":
        pass
    elif str(choice) == f"nested_list[{outer_index}][{inner_index}]":
        print("Well done, that is correct.")
        continue_playing()
    else:
        print("Incorrect. Please try again.")
        exit()

def level_four():
    outer_key = f"outer_{randint(1, 3)}"  # Random key for the outer dictionary
    inner_key = f"inner_{randint(1, 3)}"  # Random key for the inner dictionary
    nested_dict = {f"outer_{i}": {f"inner_{j}": j for j in range(1, 4)} for i in range(1, 4)}
    print(f"\nThis is the nested dictionary for the fourth level: \n{nested_dict}")
    choice = input(f"Please write the syntax for retrieving the value of '{inner_key}' from the dictionary '{outer_key}' in the nested dictionary called 'nested_dict', which in this case is {nested_dict[outer_key][inner_key]}:\n")
    if choice == "show":
        print(f"\nHere is the data structure again:\n{nested_dict}")
        level_four()
    elif choice == "skip":
        pass
    elif str(choice) == f"nested_dict['{outer_key}']['{inner_key}']":
        print("Well done, that is correct.")
        continue_playing()
    else:
        print("Incorrect. Please try again.")
        exit()


def level_five():
    # Random selections for each level of nesting
    outer_key = f"outer_key_{randint(1, 2)}"
    inner_list_index = randint(0, 1)  # Index for the inner list
    mid_key = f"mid_key_{randint(1, 2)}"
    nested_key = f"nested_key_{randint(1, 2)}"

    # Constructing a unique complex structure
    complex_structure = {
        "outer_key_1": {
            f"inner_list_{randint(1, 2)}": [
                {f"mid_key_{randint(1, 2)}": {
                    f"nested_key_{randint(1, 2)}": f"value_{randint(1, 10)}"
                }}
            ]
        },
        "outer_key_2": {
            f"inner_list_{randint(3, 4)}": [
                {f"mid_key_{randint(3, 4)}": {
                    f"nested_key_{randint(3, 4)}": f"value_{randint(11, 20)}"
                }}
            ]
        }
    }

    selected_value = complex_structure[outer_key][f"inner_list_{inner_list_index + 1}"][0][mid_key][nested_key]
    print(f"\nThis is the complex structure for the fifth level: \n{complex_structure}")
    choice = input(f"Please write the syntax for retrieving the value '{selected_value}' in the nested structure called 'complex_structure', located at {outer_key}, inner list {inner_list_index + 1}, {mid_key}, {nested_key}:\n")
    
    if choice == "show":
        print(f"\nHere is the data structure again:\n{complex_structure}")
        level_five()
    elif choice == "skip":
        pass
    elif str(choice) == f"complex_structure['{outer_key}']['inner_list_{inner_list_index + 1}'][0]['{mid_key}']['{nested_key}']":
        print("Well done, that is correct.")
    else:
        print("Incorrect. Please try again.")
        exit()



print("Begin!\nI would like you to select the correct syntax to retrieve the values from the following lists and dictionaries.\nThey will get more complex, and soon will nest inside of lists and other dictionaries.\nIf you type 'show', it will show the data structure.")

level_one()
level_two()
level_three()
level_four()
level_five()

print("You have done excellently. Well done.")