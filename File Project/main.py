# file=open("C:\python\Angelia\Day_24_File Project\my_file.txt")
# content=file.read()
# print(content)
# file.close()

# with open("Angelia\Day_24_File Project\my_file.txt") as file:
#     content=file.read()
#     print(content)

with open("Angelia\Day_24_File Project\my_file.txt",mode="a") as file:
    file.write("\n New text")
    