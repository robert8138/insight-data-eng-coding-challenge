from collections import defaultdict
import sys

# First, read in all the tweets, one tweet at a time
# For each tweet, tokenize it by separating on whitespace
# For each word in each tweet, count up using defaultdict

def generate_word_frequency(INPUT_PATH):
	'''
		generate_word_frequency process a file of tweets and generate word count
		from the corpus

		input: INPUT_PATH which is a string that represent the path to the data
		output: a dictionary with k = token, v = frequency of occurrence of k
	'''
	# Create a Defaultdict to store k,v pairs where
	# k = tokenized word
	# v = the number of times k appeared from the corpus
	d = defaultdict(int)
	with open(INPUT_PATH, 'r') as tweets:
		for tweet in tweets:
			# Assume that the only delimiter is a white space
			tokenized_tweet = tweet.split()
			for word in tokenized_tweet:
				d[word] += 1
	return d

# Print the output of the defaultdict to a output file named ft1.txt
# Since the default string comparison is based on Lexicographical order
# which uses ASCII ordering for individual characters
# We can simply sort the keys of the defaultdict by the default string comparator

# Sort the keys in defaultdict by ASCII ordering
# Write the output into ft

def write_out_word_count(d, OUTPUT_PATH):
	'''
		write_out_word_count writes the word frequency according to Lexicographical order
		input: d, a dictionary of work count
		       OUTPUT_PATH, the output file path
		output: NONE
	'''
	PADDING = 28
	with open (OUTPUT_PATH, 'w') as output:
		sorted_keys = sorted(d)
		for w in sorted_keys[:-1]:
			output.write("{}{}\n".format(w.ljust(PADDING), d[w]))
		output.write("{}{}".format(sorted_keys[-1].ljust(PADDING), d[w]))

def main():
	INPUT_PATH = sys.argv[1]
	OUTPUT_PATH = sys.argv[2]
	word_count = generate_word_frequency(INPUT_PATH)
	write_out_word_count(word_count, OUTPUT_PATH)


if __name__ == '__main__':
	main()