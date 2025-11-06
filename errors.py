# Some types of errors that are common in Python 
#Syntax Error - invalid code is present 
#NameError - trying to use a variable without declaring it first
#TypeError - the data type that is used doesn't suit what you're trying to do

#Syntax Error
# It can be something such as misspelled keyword, missing a colon (;) or missing closing parenthesis
# So great that it shows errors right away (sometimes)!

#NameError
# This can be something if I try to refer to a variable that hasn't been defined/created.
# It can also be misspelling or forgot to define it

#TypeError
#Another common error that when working with variables of various data types

#msg = 'The airs quality is '
#print(msg + 28) 

#This won't show up immediately like Syntax or Name error, though running in the terminal will

#Task
#Find the bugs in the code
#Hint: Convert numbers into string by using function str()

# Before
 
#butterflies = 10
#beetles = 12
#ladybugs = 20

#print('I caught ' + butterflies + ' 🦋 butterflies!')
#print('I caught ' + beetles + ' 🪲 beetles!')
#print('I caught ' + ladybug + ' 🐞 ladybugs!)

#print('I caught ' + str(total) + ' total bugs!'

#After

butterflies = 10
beetles = 12
ladybugs = 20 #Adding missing letter

total = butterflies + beetles + ladybugs #define total variable

print('I caught ' + str(butterflies) + ' 🦋 butterflies!') #add str() for each 
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

print('I caught ' , str(total) + ' total bugs!')