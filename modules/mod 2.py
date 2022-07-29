# import mod1
#
# print("Mod2", __name__)
# print("Mod2", mod1.__name__)


# file = open("hello.txt", mode="w", encoding="utf-8")
#
# file.write("I love Bobybuilding\n")
# file.write("I love Software Engineering\n")
# file.writelines(["i am prone to violence\n","I love Jesus"])
# file.close()


# with open("hello.txt", mode="a", encoding="utf-8") as file:
#
#     file.write("I love Bobybuilding\n")
#     file.write("I love Software Engineering\n")
#     file.writelines(["i am prone to violence\n","I love Jesus"])

with open("hello.txt", mode="r", encoding="utf-8") as file:
    for index, line in enumerate(file.readlines()):
        print(f"line {index + 1}: {line}")