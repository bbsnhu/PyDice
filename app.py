import random


def main():
    active = True
    selections = ['1', '2']
    while active:
        show_menu()
        user_input = input("Please Enter Your Selection: ")

        if user_input not in selections:
            print("Error: Invalid Selection, Please Try Again.")

        if user_input == '1':
            print("Dice Roll:", random.randint(1, 6))
        if user_input == '2':
            print("Bye")
            active = False


def show_menu():
    print("""
    1. Roll Dice
    2. Exit   
    """)


if __name__ == "__main__":
    main()
