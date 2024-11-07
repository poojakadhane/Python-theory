#Input function takes input from console or terminal from the user and execute.

# user_input = input("something:")
# print(user_input)
# name=input("what is your name?")
# print("Hello," + name + "!")

#height = input("enter your height in meter:")
# print=("your height is" +height + "meters")

age=input("enter your age")
if age.isdigit():
    age=int(age)
    print("you are" + str(age) +" years old")
else:
    print("invalid input! please enter a number")