user_name1=input("Enter your name: ")
password1=input("Create a password: ")

print("Account created.")

user_name2=input("Enter your name: ")
password2=input("Enter your password: ")

if (user_name1==user_name2 and password1==password2):
    print("You have logged in successfully!")
else:
    print("Details not found")

