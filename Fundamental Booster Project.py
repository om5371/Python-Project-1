from datetime import datetime
print("Welcome to the Interavtive Personal Data Collector")

name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))
height = float(input("Please Enter your height in meters : "))
favorite_number = int(input("Please Enter your favorite number: "))
currentyear = datetime.now().year
print("Thank you! Here is the information we collected:")


print("Name:",(name),"( Type:",type(name),"Memory Address:",id(name),")",)


print("Age:",(age),"( Type:",type(age),"Memory Address:",id(age),")",)



print("Height:",(height),"( Type:",type(height),"Memory Address:",id(height),")",)


print("Favorite Number:",(favorite_number),"( Type:",type(favorite_number),"Memory Address:",id(favorite_number),")",)
birthday = currentyear - age
print("Your birth year is approximately: ",birthday)

print("Thank You for using the Personal Data Collector. Goodbye!")