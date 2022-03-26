import datetime
# from dbms import select


# def datevalidation(date):
#     from datetime import datetime
#
#     # initializing format
#     format = "%d-%m-%Y"
#
#     res = True
#
#     # using try-except to check for truth value
#     try:
#         res = bool(datetime.strptime(date, format))
#     except ValueError:
#         email = input("enter valid date : ")
#         return datevalidation()

def createproject():
    projectid = input("ID : ")
    title = input("Title : ")
    details = input("Details : ")
    target = input("Total Target : ")
    start = input("Start Time : ")
    # datevalidation(start)
    end = input("End Time : ")
    # datevalidation(end)

    with open("project.txt", 'r') as fp:
        info = fp.read()
    if projectid in info:
        print("project already exist")
        # return select()
    else:
        projectfile = open('project.txt', 'a')
        projectinfo = {"id" : projectid , "title" : title , "details" : details , "target" : target , "start" : start , "end" : end}
        projectfile.write(f"{projectinfo}  \n")
        projectfile.close()
        f = open("project.txt", "r")
        print(f.read())
        # return select()
