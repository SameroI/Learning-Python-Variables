# if statments are blocks of code that will execute if a condtion is "true"

age = int(input("Enter your age: "))

if age == 100:
    print("You're old!")
elif age >= 18:  # checks for this condition
    print("You are legaly an adult")
elif age < 0:  # allows for a differnt check
    print("How did you type that??")
else:  # will happen if condition is not met
    print("You are not legaly an adult")
