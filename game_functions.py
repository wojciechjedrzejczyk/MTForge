import random
from models import User
from database import Database

db = Database()

def login(user: User = None) -> User:
    if user is None:
        print("---=== Witaj w świecie tabliczki mnożenia ===---\n")
        while True:
            username = input("Podaj swoje imię: ").strip()
            if username:
                break
            print("Musisz podać nazwę użytkownika!")

        user = User(username, 0)
        db_user = db.get_user(user.username)
        if db_user:
            user.score = db.get_score(user.username) or 0
            print(f"Witaj {user}!")
        else:
            db.add_user(user.username)
            print(f"Witaj {user.username} w naszym świecie!")
    else:
        print(f"Witaj {user.username}")
        print(f"Masz {user.score} punkty.\n")
        print(f"Sprawdzimy Twoją wiedze ponownie!\n")
        input()

    return user

def game(user: User = None):
    user = login(user)

    for i in range(1, 11):
        f_num = random.randint(1, 9)
        s_num = random.randint(1, 9)

        while True:
            result = input(f"{i}. {f_num} * {s_num} = \n")
            try:
                result = int(result)
                break
            except ValueError:
                print("Proszę wpisać liczbę całkowitą!")

        if result == f_num * s_num:
            print("Wynik prawidłowy!\n")
            User.add_score(user, 1)
        else:
            print("Zła odpowiedź\n")
            User.remove_score(user, 1)
            if user.score < 0:
                print("Koniec gry!\n")
                return
        db.update_score(user.username, user.score)
        print(f"Doświadczenie: {user.score}\n")

    print(f"Zakończyłeś wyzwanie, udało Ci się zdobyć "
          f"{user.score} punktów doświadczenia.\n")

    if input("Wciśnij 1 żeby kontynuować, lub dowolny inny klawisz, "
             "żeby wrócić do menu.\n") == "1":
        game(user=user)

def login_menu():
    print("1. Start")
    print("2. Wyjście\n")