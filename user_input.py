# you can assign user input to variables
# input will accept as a string so you will need to convert using type casting

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))

age = age + 1

print("Hello " + name)
print("You will be " + str(age))
print("You are " + str(height) + " feet tall")
