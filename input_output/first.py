# INPUT 
# python provides simple ways ways to interact with users through the console(terminal).
# you can display infomation using the print() function.
# And get information from users using the input() function.

# DISPLAYING OUTPUT WITH PRINT()
# The print function is the main tool for displaying information to the user:
print("hello world")
# you can print multiple items by seperating them with commas:
name = "amar"
age = 24
print("name:", name, "age:", age)

# python automatically adds spaces between the items.
# This is convenient but you can control it if needed.

# SPECIAL CHARACTERS IN STRINGS
# sometimes you need to include special characters in your output.

print("first line\nsecond line")
# \n creates a new line

print("name:\tjohn")
# \t creates a new tab

print("she said \"HELLO!\"")
# "\" allows quotes ("") inside a string

print("C:\\program files\\python")
# displays a single backslash (\)

# CUSTOMIZING PRINT BEHAVIOR
# The print() function has parameters that let you customize its behavior.

print("hello", end =" ")
print("world")

print("apple","banana","cat", sep =",")

# GETTING INPUT WITH INPUT()
# to get information from the user, use the input() function.
name = input("enter you name: ")
print(f"hello {name}")

# The input() fuction
# 1) displays the prompt
# 2)waits for the user to type something and press enter
# 3)returns the awht user typed as a string

# NOTE : The input function always returns the string.even if the user enters a number