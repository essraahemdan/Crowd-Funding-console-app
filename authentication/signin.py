from project import dbms

def login():
    username = input("enter ur name : ")
    password = input("enter password : ")
    with open("reg.txt", 'r') as fp:
        info = fp.readline()
        if username and password in info:

            return dbms()
        else:
            print("invalid username or password")
            return login()

    print("I am the login")
