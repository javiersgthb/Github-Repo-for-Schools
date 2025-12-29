first_name = input("Please enter your First Name:")
last_name = input("Please enter your Last Name:")
current_year = input("Please enter the Current Year:")
birth_year = input("Please enter your Birth Year:")
age = int(current_year) - int(birth_year)
print("Hello " + first_name + " " + last_name + "!\nYou are " + str(age) + " years old this year.")
age += 1
print("Next year, you will be " + str(age) + " years old.")
print("Written by Javier Silva")