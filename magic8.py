#The Magic 8 Ball is a popular office toy and children's
# toy invented in the 1940s for fortune-telling and advice seeking. 🎱
# Create a magic8.py program that can respond to 
# any Yes or No questions with a different answer each time it executes.



import random 

ask = input('What it is your seek answer to?:   ')

num = random.randint(1, 9)

if num == 1:
    answer = 'Yes - definitely.'
elif num == 2:
    answer = 'It is decidely so.'
elif num == 3:
    answer = 'Without a doubt.'
elif num == 4:
    answer = 'Ask again later.'
elif num == 5:
    answer = 'Better not tell you now.'
elif num == 6:
    answer = 'My sources say no.'
elif num == 7:
    answer = 'It is decidely so.'
elif num == 8:
    answer = 'Outlook not so good.'
elif num == 9:
    answer = 'Very doubtful.'
else: 
    answer = 'Error'

print('Answer: ' + answer)