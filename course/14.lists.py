# lists

food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food)
print(food[0])
print(food[-1])

food[0] = "sushi"
print(food[0])

for x in food:
    print(x, end="")
    
food.append("pizza")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()