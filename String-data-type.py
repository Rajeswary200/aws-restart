print("String data type with example \n-----------------------------\n")
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print("\nworking with string concatenation \n-------------------------------- ")
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("\nworking with input string \n--------------------------")
name = input("What is your name? ")
print(name)
print("\nformatting output string \n-------------------------------")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
