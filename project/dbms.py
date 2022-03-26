from project.create import createproject
from project.list import list
from project.edit import edit
from project.delete import delete
def select():
    while True:
            selection = input("""Please Select  
                1: create 
                2: list
                3: edit
                4: delete
                5: exit
                => """)
            if selection == '1':
                createproject()
            elif selection == '2':
                list()
            elif selection == '3':
                edit()
            elif selection == '4':
                delete()
            elif selection == '5':
                break
            else:
                print("Unknown Option Selected!")
select()