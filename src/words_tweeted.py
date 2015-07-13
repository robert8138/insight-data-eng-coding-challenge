# Create a Defaultdict to store k,v pairs where
# k = tokenized word
# v = the number of times k appeared from the corpus
import operator
from collections import defaultdict
d = defaultdict(int)

# Setup to read tweets.txt from the proper location
BASE_DIR = './../'
TWEET_INPUT_DIR = 'tweet_input/'
TWEET_OUTPUT_DIR = 'tweet_output/'
TWEET_DATA = 'tweets.txt'
INPUT_FILE_PATH = BASE_DIR + TWEET_INPUT_DIR + TWEET_DATA
OUTPUT_FILE_NAME = 'ft1.txt'
OUTPUT_FILE_PATH = BASE_DIR + TWEET_OUTPUT_DIR + OUTPUT_FILE_NAME
PADDING = 28
# First, read in all the tweets, one tweet at a time
# For each tweet, tokenize it by separating on whitespace
# For each word in each tweet, count up using defaultdict
with open(FILE_PATH) as input_f:
	for tweet in input_f:
		tokenized_tweet = tweet.split()
		for word in tokenized_tweet:
			print word
			d[word] += 1
		print '----next tweet-----'

# Print the output of the defaultdict to a output file named ft1.txt
# Since the default string comparison is based on Lexicographical order
# which uses ASCII ordering for individual characters
# We can simply sort the keys of the defaultdict by the default string comparator

# Sort the keys in defaultdict by ASCII ordering
# Write the output into ft
with open (OUTPUT_FILE_PATH,'w') as output_f:
	sorted_keys = sorted(d)
	for w in sorted_keys[:-1]:
		output_f.write("{}{}\n".format(w.ljust(PADDING), d[w]))
	output_f.write("{}{}".format(sorted_keys[-1].ljust(PADDING), d[w]))
