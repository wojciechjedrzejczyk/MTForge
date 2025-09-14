from game_functions import *

while True:
    login_menu()
    choice = input("Wybierz opcje: ")

    options = {
        "1": lambda: game(),
        "2": exit
    }

    try:
        options[choice]()
    except KeyError:
        print("Wrong key!")
    except Exception as e:
        print(f"Whats wrong: {e}")
