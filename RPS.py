from random import randint
import sys

if sys.version_info[0] == 2:
	input = raw_input

playas_choice = input ('This is a rock, paper, scissors game, choose one of the 3: ')
choices = ('rock','paper','scissors')

def pc_choice():
	pc = randint(0, 2)
	choices = ('rock', 'paper', 'scissors')
	return choices[pc]

pc = pc_choice()

print (pcs)

while playas_choice not in choices:
	playas_choice = input('Sorry i didnt understand what you meant. Pls try again: ')
	
while playas_choice == pcs:
	print ('Its a draw')
	choice = input('Do you want to try again?(yes or no) ')
	if choice.lower() == 'no':
		break
	if choice.lower() == 'yes':
		pcs = pc_choice()
		print (pcs)
		playas_choice = input('Choose beetween rock, paper. or scissors: ')

if playas_choice.lower() == 'scissors' and pcs == 'paper':
	print ('You won this one!')
elif playas_choice.lower() == 'paper' and pcs =='scissors':
	print ('You lost this one!')
elif playas_choice.lower() == 'rock' and pcs == 'scissors':
	print ('You won this one!')
elif playas_choice.lower() == 'scissors' and pcs() == 'rock':
	print ('You lost this one!')
elif playas_choice.lower() == 'paper' and pcs == 'rock':
	print ('You won this one!')

