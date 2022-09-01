from random import choice
from urllib import request
import wordle

# wordlist
wordlist_url = "https://gist.githubusercontent.com/shmookey/b28e342e1b1756c4700f42f17102c2ff/raw/ed4c33a168027aa1e448c579c8383fe20a3a6225/WORDS"
wordlist = request.urlopen(wordlist_url).read().decode().split('\n')[:-1] # :-1 to strip empty string

# game variables
tries = 0

if __name__ == "__main__":
	random_word = choice(wordlist)

	print(f"Word length: {len(random_word)}")

	while tries < 6:
		attempt = input("Word: ")

		if len(attempt) == len(random_word):
			if attempt in wordlist:
				if wordle.check(random_word, attempt):
					print(f"Completed in {tries} tries!")
					break
				else:
					tries += 1
			else:
				print("Not in wordlist!")
					
	print(f"The word was: {random_word}")
		