

#i'll be input user name,age,house number,and street name

user_name = input ("please enter your name? ")
user_age = input ("Please enter your age? ")
user_house_number = input("Please enter your house number? ")
user_street_name = input("Please enter your street name? ")

#And i'll be printing out a single sentence containing all the user details 

user_details = "Hello! My name is {} , I am {} yers old, and i live at {}.".format(user_name, user_age, user_house_number, user_street_name)
print(user_details)
