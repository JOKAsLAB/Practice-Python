# string format

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)

print("The {} jumped over the {}.".format(animal,item))
print("The {1} jumped over the {0}.".format(item,animal))
print("The {ANIMAL} jumped over the {ITEM}.".format(ANIMAL="cow",ITEM="moon"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

print()
# ---------------------------------------------------

name = "Joca"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

print()
# ---------------------------------------------------

number1 = 3.14159

print("The number pi is {:.1f}".format(number1))
print("The number pi is {:.2f}".format(number1))
print("The number pi is {:.3f}".format(number1))

number2 = 1000

print("The number pi is {:,}".format(number2))
print("The number pi is {:b}".format(number2))
print("The number pi is {:o}".format(number2))
print("The number pi is {:X}".format(number2))
print("The number pi is {:E}".format(number2))