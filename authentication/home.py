from authentication.signin import login
from authentication.signup import register

def mainfunction():
    choice = input("Plz enter your choice log or reg ")
    if choice == "log" or choice == "reg":
        if choice == "log":
            return login()
        else:
            return register()

    return mainfunction()

mainfunction()