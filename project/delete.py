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
def delete():
    findproject()
    projectfile = open('project.txt', 'w')
    for i in lst:
        var = eval(i)
        if var["id"] != projectdict["id"]:
            projectfile.write(f"{var} \n")
    projectfile.close()
