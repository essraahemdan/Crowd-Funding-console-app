from project.create import createproject
projectdict = {}
lst = []
def findproject():
    global projectdict , lst
    projectid = input("enter ID : ")
    with open("project.txt", 'r') as fp:
        lst = fp.readlines()
        print(lst)
    for p in lst:
        project = eval(p)
        if project["id"] == projectid:
            projectdict = project
            return True
    else:
        print("project not exist")
        return findproject()
# and project["user"] == firstname
def edit():
    global projectdict
    findproject()
    while True:
        selection = input("""Please Select:
                1: title 
                2: details
                3: target
                4: start
                5: end
                6: exit
                => """)
        if selection == '1':
            projectdict["title"] = input("title")
        elif selection == '2':
            projectdict["details"] = input("details")
        elif selection == '3':
            projectdict["target"] = input("target")
        elif selection == '4':
            projectdict["start"] = input("start")
        elif selection == '5':
            projectdict["end"] = input("end")
        elif selection == '6':
            break
        else:
            print("Unknown Option Selected!")
    projectfile = open('project.txt', 'w')
    for i in lst:
        var = eval(i)
        if var["id"] == projectdict["id"]:
            projectfile.write(f"{projectdict} \n")
        else:
            projectfile.write(f"{var} \n")
    projectfile.close()

