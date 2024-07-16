# sets

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)
    
print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))