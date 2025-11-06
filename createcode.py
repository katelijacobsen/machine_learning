# Data Types 
# We use variables to store data values. Each variable holds a name and holds a value. 
# It can be compared to a slap on a label, and it can store stuff.

# For example, similar to JavaScript: 

name = 'Earl Bachman'  # string value. Its simple and stores text. Can either be wrapped in " " or ''. 
user_id = 12345678 #Integer (int), is a whole number. It doesn't use decimal numbers and contains the number 0 (positive and negative)
# As an example, we could use this type of variable such as counting or the number amount of how many balls are in a jar. 
progress = 0.67 # This variable is called a float-point number (float), which uses a decimal number. Can be used for measurements or representing fractions.
#Good for using percentage, calculations or measuring sizes of objects.
xp = 20
verified = True #Boolean what can be toggled between true or false, there is nothing in between. See it as black and white.
#This value is capitalized in Python. Fun fact: its named after the british mathematician George Boole (hehehe)



# Operaturs
# Python uses arithmetic operators to calculate different things (arithmetic meaning the most basic branch of mathematics to deal with numbers)

#These are the arithmetic operators : 
# + Addition
# - Subtraction
# * Multiplication
# / Division

# Specific explaination to modulo & exponents operators

# % Modulo
# It doesn't give you the result of a division but the remainder (part of something that is left over when other parts have been completed, used or dealth with).

# ** Exponents
# Similar to multiplication. In written math, se see it as a superscript number.
# Imagine, 10 ** 2 is 10^2 (2 is the tiny small number)

mass = 85
height = 1.77

bmi = mass/height**2

print(bmi)