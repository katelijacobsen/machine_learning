# For Loop
# This type of loop decides how many times it should repeat.
# By adding a variant and using a function called range(), we can decide
# how many times it repeats.



for i in range(5):
    print(i)
print('this line is not looping')


for i in range(5):
    print(i)
    print('this line is looping')

# While Loop (+ if statement)
# A while loop is like keep on doing a task until it is done.
# Compare it when watering plants: you're watering until you have no water left
password = ""

while password != "chicken":
    password = input("Enter password:   ")
    if password != "chicken":
        print("wrong")
print("Login successful")


for x in "Hej med dig":
    print(x)


# For Loop example where it starts from 5, prints 3 numbers and excludes 7.
# The output will be 5 6 6
for x in range(5,7):
    print(x)
else:
    print(x)

# This type of loop adds another int for the variable
for x in range(1,7):
    x = x + 1 #adds 1 to 1
    print(x)

# Don't look

pw = ""

while pw != "underpants":
    pw = input('Enter your password please:     ')
    if pw != "underpants":
        print('Oh no, wrong password :(')
    if pw == "underpants":
        print('Nice, you are now logged in :)')