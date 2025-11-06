
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0



Q1 = int(input('Q1) Do you like Dawn or Dusk?\n\t1) Dawn\n\t2) Dusk\n'))

if Q1 == 1:
   gryffindor +=  1
   ravenclaw  += 1
elif Q1 == 2: 
   hufflepuff += 1
   slytherin += 1
else:
   print('WRROONNNNG')

Q2 = int(input('When I am dead, I want people to remember me as\n\t1) The Good\n\t2) The Great\n\t3) The Wise\n\t4) The Baddie'))

if Q2 == 1:
   hufflepuff += 2
elif Q2 == 2:
   slytherin += 2
elif Q2 == 3:
   ravenclaw  += 2
elif Q2 == 4:
   gryffindor +=  2
else:
   print('WroooooondsfgonDAFK')

Q3 = int(input('Which kind of instrument most pleases your ear?\n\t1) The violin\n\t2) The trumpet\n\t3) The piano\n\t4) The drum'))

if Q3 == 1:
   slytherin += 4
elif Q3 == 2:
   hufflepuff += 4
elif Q3 == 3:
   ravenclaw  += 4
elif Q3 == 4:
   gryffindor +=  4
else:
   print('WroooooondsfgonDAFK')

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
   print('Miau min bror, du gryffindor fordi du har opjent ' + str(gryffindor) + ' point')
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
   print('KAWWWKAAAAAAAW min bror, du er en flot fugl og har optjent ' + str(ravenclaw) + ' point')
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin: 
   print('GRUM GRUM min bror du har tjent ' + str(hufflepuff) + ' point, brormand')
else:
   print('SSS SSSS SSSS fucking slange ' + str(slytherin) + ' point')