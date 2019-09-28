def main():
	print('HANGMAN THE GAME')
	print('||||| Player 1 |||||')
	word = input('Please enter a word: ')

	# Hide input or clear screen
	for i in range(500):
		print('')

	print('----- Player 2 -----')

	# correct_guesses tracks the correct
	# guesses of player 2
	correct_guesses = []
	incorrect_guesses = []
	count = 0 # number of letters guessed
	a = '' # string containing player's guess progress
	wrong = 0

	b = '' # string containing underscores to represent the length of the word
	for i in range(len(word)):
		b = b + '_'
	print('Try to guess: ' + b)

	while True:

		if count == len(word):
			print('Congratulations, you won!')
			break
		letter = input('Guess a letter: ')
		ct = [] # count tracker
		# correct guess
		if letter in word:
			print('Yes! The word contains: {}'.format(letter))

			if letter not in correct_guesses:
				count = count + word.count(letter)
			correct_guesses.append(letter)
			a = ''
			for char in word:
				if char in correct_guesses:
					a = a + char
				else:
					a = a + '_'
			print(a)

		# incorrect guess
		else:
			incorrect_guesses.append(letter)
			wrong=wrong+1
			print('No.. that\'s {} incorrect guess(es)'.format(wrong))
			print_hangman(wrong)
			print('Incorrect guesses: {}'.format(', '. join(incorrect_guesses)))
			if wrong == 6:
				print('The word was: {}'.format(word))
				print('I\'m sorry, you lose. Better luck next time.')
				break

def print_hangman(wrong):
	if wrong == 0:
		pass
	elif wrong == 1:
		print('  -------')
		print('  |     !')
		print('  |     O')
		print('  |')
		print('  |')
		print('  |')
		print('  |')
		print('\/\\/\\/\\/\\/\\/\\')
	elif wrong == 2:
		print('  -------')
		print('  |     !')
		print('  |     O')
		print('  |     |')
		print('  |     |')
		print('  |')
		print('  |')
		print('\/\\/\\/\\/\\/\\/\\')
	elif wrong == 3:
		print('  -------')
		print('  |     !')
		print('  |     O')
		print('  |   \_|')
		print('  |     |')
		print('  |')
		print('  |')
		print('\/\\/\\/\\/\\/\\/\\')
	elif wrong == 4:
		print('  -------')
		print('  |     !')
		print('  |     O')
		print('  |   \_|_/')
		print('  |     |')
		print('  |')
		print('  |')
		print('\/\\/\\/\\/\\/\\/\\')
	elif wrong == 5:
		print('  -------')
		print('  |     !')
		print('  |     O')
		print('  |   \_|_/')
		print('  |     |')
		print('  |   _/')
		print('  |')
		print('\/\\/\\/\\/\\/\\/\\')
	elif wrong == 6:
		print('  -------')
		print('  |     !')
		print('  |     O')
		print('  |   \_|_/')
		print('  |     |')
		print('  |   _/ \_')
		print('  |')
		print('\/\\/\\/\\/\\/\\/\\')
if __name__ == "__main__":
	main()
