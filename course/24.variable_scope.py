# variable scope

name = "Joca"

def display_name():
    name = "Martins"
    print(name)
    
display_name()
print(name)