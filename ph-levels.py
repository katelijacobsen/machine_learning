# Python has both arithmetic and relational operators. 
# Since we know the arithmetic ones (+, -, * and /), the relational operators compares the values

# Definition of relational operators 
# == equal to
# != not equal to
# > greater than
# < less than
# >= more or equal to
# <= less or equal to

# Elif
# Since we shortly have learned the if statement in Python and it also includes an else,
# it has also the possibility to include the elif, short for else if. 
# This allows to have multiple states in the if. Of course only one of the options will execute.

# Task
# In chemistry, pH is a scale used to specify the acidity or basicity of a liquid. 🧪

# Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.
# First, create a ph variable and ask the user for a value between 0 and 14.

# Write an if, elif, else statement that:

# If ph is greater than 7, output "Basic"
# If ph is less than 7, output "Acidic"
# Else, output "Neutral"

ph = int(input('What is the ph level? (0-14:)'))

if ph > 7: 
    print('Basic')
elif ph < 7:
    print('Acidic')
else: print('Neutral')