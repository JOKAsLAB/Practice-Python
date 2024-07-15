# logical operators

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("go toutch some grass")
elif temp < 0 or temp > 30:
    print("stay inside! do not go out!")
    
if not (temp >= 0 and temp <= 30):
    print("stay inside! do not go out!")
elif not (temp < 0 or temp > 30):
    print("go toutch some grass")