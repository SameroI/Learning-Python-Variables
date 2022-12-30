# logical operators (and,or,not) are used to check if two or more conditional statments are true

temp = int(input("Enter the outside temperature: "))

# for "not" suround your statment in () and preseed with not, it will "flip" the true and false of the statment

if temp >= 0 and temp <= 30:  # both conditions must be true
    print("The weather is nice!")
    print("You should head out for a bit!")
elif temp < 0 or temp > 30:  # one or the other must be true
    print("Weather is not safe!!")
    print("Stay in today!")
