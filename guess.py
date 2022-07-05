import random
import sys

start = sys.argv[1]
end = sys.argv[2]

start = int(start)
end = int(end)

def repeat():
	choose = input(f'Choose a number between {start} and {end}.')
	choose = int(choose)
	gold_list = list(range(start, end))
	truth = random.choice(gold_list)
	print(f'The answer is {truth}.')
	print(f'You guessed {choose}')

	if choose != truth:
		repeat()
	else:
		print('You are a genius!')
		exit()

repeat()
