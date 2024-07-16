# dictionary

capitals = { "USA" : "Washington DC",
             "India" : "New Dehli",
             "China" : "Beijing",
             "Russia" : "Moscow"}

capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "Las Vegas"})
capitals.pop("India")

print(capitals["China"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

print()

for key, value in capitals.items():
    print(key, value, end=", ")