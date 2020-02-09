import numpy as np
import random

#Pulling functions
from sendingEmail import send

names = np.array( ['User1', 'User2', 'User3', 'User4', 'User5'] )
emails = np.array(['User1@emailaddress.com', 'User2@emailaddress.com', 'User3@emailaddress.com', 'User4@emailaddress.com' , 'User5@emailaddress.com'])
position = np.arange(names.size)

l = list(range(names.size))

x = 0
while x != names.size:

	if (x == 0): #Shuffling both arrays to ensure randomization
		random.shuffle(l)	
		random.shuffle(position)
		x = x + 1
	elif (l[x-1] == position[x-1] or l[x] == position[x]):
		print("Re-evaluating...")
		x = 0
	else:
		x = x + 1

#Numerical Verification printed below
print(position)
print(l)

#If you would like to ensure that algorithm matches users properly the uncomment the below lines
#print(names)
#print(names[l])

secret_santa = names[l]

for x in range(len(names)):
	print(names[x] + " - " + emails[x] )

proceed = input("\nDoes this information look correct? (y/n): ")

if (proceed == 'y'):
	send(names, emails, secret_santa)	