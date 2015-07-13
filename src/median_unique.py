# Create a Defaultdict to store k,v pairs where
# k = tokenized word
# v = the number of times k appeared from the corpus
from numpy import median
from collections import defaultdict
d = defaultdict(set)


# Setup to read tweets.txt from the proper location
BASE_DIR = './../'
TWEET_INPUT_DIR = 'tweet_input/'
TWEET_OUTPUT_DIR = 'tweet_output/'
TWEET_DATA = 'tweets.txt'
OUTPUT_FILE_NAME = 'ft2.txt'
INPUT_FILE_PATH = BASE_DIR + TWEET_INPUT_DIR + TWEET_DATA
OUTPUT_FILE_PATH = BASE_DIR + TWEET_OUTPUT_DIR + OUTPUT_FILE_NAME

# First, read in all the tweets, one tweet at a time
# For each tweet, tokenize it by separating on whitespace
# Then we want to count the number of unique tokens in each tweet
with open(INPUT_FILE_PATH, 'r') as input_f:
	for line_num, tweet in enumerate(input_f):
		tokenized_tweet = tweet.split()
		for word in tokenized_tweet:
			d[line_num].add(word)

# Calculate the unique number of tokens from each tweet using map
# funtional programming style for the win!
d_unique_count = map(lambda token_set: len(token_set), d.itervalues())

# Based on the list, compute a running calculation of median
#running_medians = [reduce(lambda x,y: x+y, l[:i]) for i in range(1, len(l)+1)]
running_medians = [median(d_unique_count[:i]) for i in range(1, len(d_unique_count)+1)]

with open (OUTPUT_FILE_PATH, 'w') as output_f:
	for median in running_medians[:-1]:
		output_f.write("{}\n".format(median))
	output_f.write("{}\n".format(running_medians[-1]))