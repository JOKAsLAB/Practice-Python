# tuples

student = ("Joca", 20, "male")

print(student.count("Joca"))
print(student.index("male"))

for x in student:
    print(x, end=" ")
    
print()    
    
if "Joca" in student:
    print("Joca is here!")    