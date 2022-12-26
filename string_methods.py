# string methods let you alter a givin string
name = "samero"

print(len(name))  # len prints amount of charecters
print(
    name.find("s")
)  # finds where a charecter is within a string, starts at 0 and counts up from there
print(name.capitalize())  # will capitalize the first charecter
print(name.upper())  # will make make all charecters in the string upercase
print(name.lower())  # will make all charecters in the string lowercase
print(name.isdigit())  # displays true if charecters are a digit and false if not
print(
    name.isalpha()
)  # displays true if charecters are alphabetical and false if not (SPACES WILL MAKE IT RETURN FALSE)
print(name.count("a"))  # counts the amount of specified charecters in a string
print(name.replace("e", "i"))  # replaces a specified charecter with another
print(name * 3)  # will display the string that many times
