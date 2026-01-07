# VARIABLES

# variables are containers for storing data 
# variables must start with a letter or underscore ( _ )
# varibles should only contain letters,numbers and underscores( _ )
# varbles cannot be python keywords (if,for,else,etcc)
# variables are case sensitive (age,AGE)


name = "naveen"
age = 25
print(name,age)


# DATA TYPES

# there are several data types in python 

#  1) int data type ; (int)
    # integer is whole number not a decimal number 
    # it id positiive or negative
    # python integers has unlimited precision
     
age = 24
Age = -3
print(age,Age)
      
 # 2) float data type ; (float)
    #  floats are numbers with decimal point
    #  floats has limited precision
    
float = 23.5
print(float)

 # 3)boolean data type ; (bool)
    #  booleans has only two possible values True or False
    #  true(error) always True(valid) and same for False
    
active = True
error = False 
print(active)
print(error)

 # 4)complex data type ; (complex)
    # complex numbers have real part and imaginary part
    # we can also create them using complex function
    
complex_b= (2+3j) 
complex_a =complex(5, 7)
print(complex_b)
print(complex_a.real)
print(complex_a.imag)

 # 5)string data type ; (str)
    # strings are sequence of characters, used to represent text
    # strings must contain single quotes ('') or double quotes (" ")
    # for multiline strings we use triple quotes (""" """)
    
name ='naveen'
name_1 ="naveen"
single = "i'm learning python"
double = 'he said i learn "python" today'
multi_line = """ this is multiline string
in python """
print(name)
print(name_1)
print(single)
print(double)
print(multi_line)