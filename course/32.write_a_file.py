# write a file

text = "Yooooooooooooooo\nThis is some text\nHave a good one!\n"
with open("D:\\git hub\\Practice-Python\\course\\32.test.txt", "w") as file:
    file.write(text)

text = "\nHave a nice day! See ya"
with open("D:\\git hub\\Practice-Python\\course\\32.test.txt", "a") as file:
    file.write(text)