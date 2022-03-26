def list():
    f = open("project.txt", "r")
    print(f.read())
# row_format ="{:>15}" * (len(lst) + 1)
# print(row_format.format("", *lst))
# for lst, row in zip(lst, f):
#     print(row_format.format(lst, *row))