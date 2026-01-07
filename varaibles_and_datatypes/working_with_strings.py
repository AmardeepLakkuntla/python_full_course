
# strings in python are incredibly versatile

# STRING INDEXING

# we can access individual characters in string using square brackats[ ] 
# note that indexing starts at 0
# we can also use negative indices to count from the end

text = "python"
first = text[0]
second = text[4]
last = text[-1]
last_1 = text[-3] 
print(first)
print(second)
print(last)
print(last_1)

# STRING SLICING

# slicing lets you extract one portion of a string using the syntax
 # [start:stop:step]
#  in string slicing stop index is neglected
 
text_1 = "python programming" 
string_1 = text_1[0:6]
print(string_1)
# from start index (0) to stop index -1 (6-1)(5) 

string_2 =text_1[:6]
print(string_2)
# short from startindex to 6 index(i.e 5)

string_3 = text_1[7:]
print(string_3)
# from index 7 to the end

string_4 = text_1[::2]
print(string_4)
# every sencond character (it skips one and takes one for every step )

string_5 =text_1[::-1]
print(string_5)
# it is reversed string it tskes each step from reversed order

# STRING METHODS
# python strings come with many built-in methods:

# CASE CONVERSION
text_2 = "hello, world!"
upper_1 = text_2.upper()
print(upper_1)
# upper is the conversion of the characters into capital letters

lower_1 = text_2.lower()
print(lower_1) 
# lower is the conversion of the characters into small letters

title_1 = text_2.title()
print(title_1)
# title is the conversion of the characters that for every word the first leter will capital and the other are small

capitalize_1 = text_2.capitalize()
print(capitalize_1)
# capitalize is the conversion of the characters that for sentence the first letter will be capital

swap = text_2.swapcase()
print(swap)
# swapcase is the conversion of the characters that it will swap from capital to small letters and vice verca

# SEARCHING AND REPLACING
contains = "world" in text_2
print(contains)
#  in makes is the text_! contain the given word ...(True or False)

position = text_1.find("python")
print(position)
# if it finds the given word then it prints the starting index of the word
# if any one letter in word does not matches or not found the given word then it returns -1 (not found)

count_1 = text_1.count("p")
print(count_1)
# counts the given letter or word in list and returns their count

replaced = text_2.replace("world","amar")
print(replaced)
# replaces the old word with the new given word( , separates the old word and new word)

# WHIESPACE HANDLING
text_3 = " hello, world  "
stripped = text_3.strip()
left_strip = text_3.lstrip()
right_strip = text_3.rstrip()
print(stripped)
print(left_strip)
print(right_strip)
# strip( ) removes the space in between them or extra space
# lstrip( ) used to remove left side extra space
# rstrip( ) used to remove right side extra space

# SPLITTING AND JOINING
text_4 = "amar shiva arun sai"
friends = text_4.split()
print(friends)
# split( ) will splits the word by default with comma( , )..and returns in the list format[ ]

friends_2 ="".join(text_4)
friends_3 =",".join(text_4)
friends_4 =" , ".join(text_4)
print(friends_2) 
print(friends_3)
print(friends_4)
# .join(should give variable) will joins the text with given thing
# in friends_3 context it joins the text with comma(,)(every letter in given text separates with comma)
# in friends_4 context it joins the text with comma(,)along with given space( ) (every letter in given text separates with comma)

# CHECKING STRING CONTENT
text_5 = "Hello123"
text_6 = "123"
text_7 = "HELLO"
text_8 = "hello world"
text_9 = " "
print(text_5.isalnum())
print(text_6.isdigit())
print(text_7.isupper())
print(text_8.islower())
print(text_9.isspace())
# is specifies if it caonatins only the specified thing (isdigit,etcc) yes or not return True or False
# isalnum() alphanumnerical (True)
# isdigit() only numbers (True)
# isupper() only upper case letters (True)
# islower() only lower case letters (True)
# isspace() is it conatins space (True)