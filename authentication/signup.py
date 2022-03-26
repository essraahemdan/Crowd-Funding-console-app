from signin import login
import re

regex =re.compile(r"[^@]+@[^@]+\.[^@]+")

def check(email):
    if (re.fullmatch(regex, email)):
            return True
    else:
        email = input("enter valid email : ")
        check(email)

def confirm ( password, confirmpass):
    if (password == confirmpass):
        return True
    else:
        password = input("enter another password : ")
        confirmpass = input("confirm password : ")
        confirm(password,confirmpass)

def register():
    firstname = input("enter ur first name : ")
    lastname = input("enter ur last name : ")
    password = input("enter ur password : ")
    confirmpass = input("confirm password : ")

    confirm(password , confirmpass)

    email = input("enter ur email : ")

    check(email)

    phone = input("enter ur phone number : ")

    with open("reg.txt", 'r') as fp:
        info = fp.readline()
    if email and password in info:
        print("u already registered")
        return login()
    else:
        file = open('reg.txt', 'w')
        file.write(firstname + "\n" + lastname + "\n" + password + "\n" + confirmpass + "\n" + email + "\n" + phone + "\n")
        file.close()
        return login()

