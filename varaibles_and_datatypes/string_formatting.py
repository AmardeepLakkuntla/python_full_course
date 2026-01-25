

# There are several ways to format strings in python

# 1) f-strings
# The most modern and readable appproach:
name = "amar"
age = 24
message = f"{name} is {age} years old"
print (message)

# 2) str.format() method
name = "amar"
age = 24
message_1 ="{} is {} years old".format(name,age)
print(message_1)

# 3) %-formatting(older style)
# this is an older style, but you may see it in existing code
name = "amar"
age = 24
message_2 = "%s is %d years old " %(name,age)
# we can also directly print this in one line 
print("%s is %d years old " %(name,age))
print(message_2) 

# format specifiers
# both f-strings and str.()format() support format specifiers for more contol

# number formatting
pi =3.14159
print(f"pi is approximately {pi:.2f}")
# adding commas as thousand separators
large_number = 1234567.89
print(f"value: {large_number:,.2f}")
# padding and allignment
print(f"{'left':<10}|{'center':^10}|{'right':>10}")