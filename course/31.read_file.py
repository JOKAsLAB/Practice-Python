# read a file

try:
    with open("D:\\git hub\\Practice-Python\\course\\31.test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :/")