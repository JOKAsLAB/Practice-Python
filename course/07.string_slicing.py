# string_slicing

#-----indexing[]-----#
name = "Joaquim Jose Fernandes Martins"

first_letter = name[0]
print(first_letter)

first_name = name[:7]
print(first_name)

last_name = name[23:]
print(last_name)

strange_name = name[0:30:3]
print(strange_name)

reversed_name = name[::-1]
print(reversed_name)


#------slice()------#
website1 = "http://youtube.com"
website2 = "http://instagram.com"

name1 = website1[slice(7, -4)]
print(name1)

name2 = website2[slice(7, -4)]
print(name2) 
