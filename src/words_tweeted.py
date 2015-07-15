## Author: Robert Chang
## Purpose: Calculate the total number of times each word has been tweeted
## Input: An input stream/file containing tweets
## Output: An output of word, frequency pairs display in lexicographical order 
## Assumptions: 
## 		1. Each tweet can be tokenized by whitespace
##      2. Each tweet has only lower case characters and regular ASCII characters
##      3. The dictionary can be fit into memory

import sys
from collections import defaultdict

def generate_word_frequency(INPUT_PATH):
	'''(string) -> defaultdict(int)

	For each tweet in INPUT_PATH, tokenize the tweet and tally up the word frequency
	'''
	d = defaultdict(int)
	with open(INPUT_PATH, 'r') as tweets:
		for tweet in tweets:
			tokenized_tweet = tweet.split()
			for word in tokenized_tweet:
				d[word] += 1
	return d

def write_word_frequency(d, OUTPUT_PATH):
	'''(defaultdict(int), string) -> None 
	
	Output the frequency of word appearances in ASCII order
	Since the default string comparison in Python is based on Lexicographical order
	which uses ASCII ordering for individual characters, we can simply sort
	the keys by using the default string comparator 
	'''
	with open (OUTPUT_PATH, 'w') as output:
		sorted_keys = sorted(d)
		for w in sorted_keys[:-1]:
			output.write("{}\t{}\n".format(w, d[w]))
		output.write("{}\t{}".format(sorted_keys[-1], d[sorted_keys[-1]]))

def main():
	INPUT_PATH = sys.argv[1]
	OUTPUT_PATH = sys.argv[2]
	word_frequencies = generate_word_frequency(INPUT_PATH)
	write_word_frequency(word_frequencies, OUTPUT_PATH)

if __name__ == '__main__':
	main()