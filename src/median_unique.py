from numpy import median
from collections import defaultdict
import sys

# First, read in all the tweets, one tweet at a time
# For each tweet, tokenize it by separating on whitespace
# Then we want to count the number of unique tokens in each tweet
def generate_unique_word_count(INPUT_PATH):
	'''
		generate_unique_word_count maps through the input file
		for each tweet, generate the unique number of tokens from that tweet
		Input: INPUT_PATH
		Output: a list of unique token count
	'''
	# Create a Defaultdict to store k,v pairs where
	# k = tokenized word
	# v = the number of times k appeared from the corpus
	d = defaultdict(set)
	with open(INPUT_PATH, 'r') as tweets:
		for line_num, tweet in enumerate(tweets):
			tokenized_tweet = tweet.split()
			for word in tokenized_tweet:
				d[line_num].add(word)

	# Calculate the unique number of tokens from each tweet using map
	# funtional programming style for the win!
	d_unique_count = map(lambda token_set: len(token_set), d.itervalues())
	return d_unique_count

def calculate_running_median(d_unique_count, OUTPUT_PATH):
	'''
		calculate_running_median process a list of unique count
		and calculate the running median
		input: d_unique_count, a list of count of unique token
		       OUTPUT_PATH, output path we are writing to
		output: None
	'''
	# Use list comprehension to calculate median 
	# This is not efficient, we can do this in one pass
	# Using one min heap and one max heap
	running_medians = [median(d_unique_count[:i]) 
							for i in range(1, len(d_unique_count)+1)]
	# Write out the running medians to OUTPUT_PATH
	with open (OUTPUT_PATH, 'w') as output:
		for med in running_medians[:-1]:
			output.write("{}\n".format(med))
		output.write("{}\n".format(running_medians[-1]))

def main():
	INPUT_PATH = sys.argv[1]
	OUTPUT_PATH = sys.argv[2]
	uniq_word_count = generate_unique_word_count(INPUT_PATH)
	calculate_running_median(uniq_word_count, OUTPUT_PATH)

if __name__ == '__main__':
	main()