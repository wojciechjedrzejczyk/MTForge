import random
from models import User

def game():
    print("---=== Witaj w świecie tabliczki mnożenia ===---\n")
    print("Dostaniesz kilka działań, za każdą poprawną odpowiedź zdobędziesz"
          "punkty doświadczenia.")
    print("Jeśli masz na tyle odwagi wciśnij Enter ...")
    input()

    user = User("Edmar", "haslo", 0)


    for i in range(1, 11):
        f_num = random.randint(1, 9)
        s_num = random.randint(1, 9)
        result = input(f"{i}. {f_num} * {s_num}= ")
        if int(result) == f_num * s_num:
            print("Wynik prawidłowy!\n")
            User.add_score(user, 1)
            print(f"Doświadczenie: {user.score}\n")
        else:
            print("Zła odpowiedź\n")
    print(f"Zakończyłeś wyzwanie udało Ci się zdobyć {user.score} punktów "
          f"doświadczenia.\n")
    if input("Wciśnij 1 żeby kontynuować, "
             "lub dowolny inny klawisz żeby wrócić do menu") == "1":
        game()



def login_menu():
    print("1. Start")
    print("2. Wyjście\n")

while True:
    login_menu()
    choice = input("Wybierz opcje: ")

    options = {
        "1": game,
        "2": exit
    }

    try:
        options[choice]()
    except KeyError:
        print("Wrong key!")
    except Exception as e:
        print(f"Whats wrong: {e}")