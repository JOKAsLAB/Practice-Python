# dictionary comprehensions

cities_in_F =   {"New York" : 32,
                 "Boston" : 75,
                 "Los Angeles": 100,
                 "Chicago" : 50}

cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

print()
print("----------------")
print()

weather = { "New York" : "snowing",
            "Boston" : "sunny",
            "Los Angles" : "sunny",
            "Chicago" : "cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

print()
print("----------------")
print()

cities =   {"New York" : 32,
            "Boston" : 75,
            "Los Angeles": 100,
            "Chicago" : 50}

desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities.items()}
print(desc_cities)

print()
print("----------------")
print()

cities =   {"New York" : 32,
            "Boston" : 75,
            "Los Angeles": 100,
            "Chicago" : 50}

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)
