# sort

students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]

students.sort()
for i in students:
    print(i)
    
print("------------")    
    
students.sort(reverse=True)
for i in students:
    print(i)
    
print("------------")    
    
students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")  
    
sorted_students = sorted(students)
for i in sorted_students:
    print(i)
    
print("------------")    
   
sorted_students = sorted(students,reverse=True)
for i in sorted_students:
    print(i)
print("------------") 

#---------------------------------------------------------------------

students = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78)
]

students.sort()
for i in students:
    print(i)
    
print("------------") 

grade = lambda grades : grades[1]
students.sort(key=grade)
for i in students:
    print(i)
    
print("------------") 

age = lambda ages : ages[2]
students.sort(key=age)
for i in students:
    print(i)

print()