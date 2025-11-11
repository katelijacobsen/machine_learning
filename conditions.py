name = input('Hvad er dit navn?     ')

if name == "Kevin":
    print('Kæft det grimt...')
else:
    print("Ejjj det et pændt navn")

tal = int(input('Skriv et tal:    '))

if tal >= 100: 
    print("Nøj, et stort tal du fandt der")
elif tal < 20:
    print('Godt nok et lille tal')
elif 20 < tal and tal < 80:
    print('mellemstort tal')
else:
    print('hvAbehar')

user = input('Indtast venligst "vits" eller "riddle":    ')

vits = "What do you call 8 hobbits? A hob-byte :')"

riddle = "What belongs to you but others use it more than you do?"

answer = "my name"

if user == "vits":    
    print(vits)

if user == "riddle":    
    print(riddle)


command = input("Skriv en kommando:   ")
print (command)


if "Error" in command: 
    print("- FEEEEEJL!")
else:
    print("- OK!")