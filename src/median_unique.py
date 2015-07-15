## Author: Robert Chang
## Purpose: Calculate the median number of unique words per tweet, and update this median as tweets come in
## Input: An input stream/file containing tweets
## Output: Running median number of unique words per tweet
## Assumptions: 
## 		1. Each tweet can be tokenized by whitespace
##      2. Each tweet has only lower case characters and regular ASCII characters

import sys
import heapq

def map_tweet_to_unique_wc(INPUT_PATH):
	'''(string) -> defaultdict(set)

	For each tweet in INPUT_PATH, tokenize the tweet and count the 
	number of unique token using Functional programming style 'Map' operation 
	'''
	with open(INPUT_PATH, 'r') as tweets:
		return map(lambda tweet: len(set(tweet.split())), tweets)

def calculate_running_median(uniq_wc_list, OUTPUT_PATH):
	'''(list, string) -> None
	
	Take one pass of the uniq_wc_list and compute running median
	using by maintaining a min-heap and a max-heap
	'''
	running_medians = []

	#Assume that there exists at least one tweet in the stream/file
	first_uniq_wc = uniq_wc_list.pop(0)

	# We will calculate the median by maintaining a min-heap and max-heap
	# This approach is preferred as we only need to take one pass of the data
	# And is better than repeatedly calculating the median on different subset of the data
	# Note: 1. The default heap from heapq is min-heap, we can construct a max-heap
	#       simply by multiplying every element by -1 
	#       2. the syntax heap[0] gives us the root element of heap
	if uniq_wc_list:
		second_uniq_wc = uniq_wc_list.pop(0)
		if first_uniq_wc >= second_uniq_wc:
			min_heap = [first_uniq_wc] 
			max_heap = [-second_uniq_wc]
		else:
			min_heap = [second_uniq_wc]
			max_heap = [-first_uniq_wc]
		running_medians.append(first_uniq_wc)
		running_medians.append(float(min_heap[0] - max_heap[0])/2)
	else:
		min_heap = [first_uniq_wc]
		running_medians.append(first_uniq_wc)

	while uniq_wc_list:
		# Process a new unique word count
		count = uniq_wc_list.pop(0)

		# Update the min-heap or max-heap to maintain the invariant that
		# the root of the min_heap is at least as big as the root of the max_heap 
		if count >= min_heap[0]:
			heapq.heappush(min_heap, count)
		elif count < -max_heap[0]: 	
			heapq.heappush(max_heap, -count)
		else:
			# this is the case where count is in between the two keys
			heapq.heappush(max_heap, -count)
		
		# Rebalance the heap structures so their size is off at most by one
		if len(max_heap) - len(min_heap) > 1:
			heapq.heappush(min_heap, -heapq.heappop(max_heap))
		elif len(min_heap) - len(max_heap) > 1:
			heapq.heappush(max_heap, -heapq.heappop(min_heap))

		# Update Median
		if len(max_heap) - len(min_heap) == 1:
			running_medians.append(-max_heap[0])
		elif len(min_heap) - len(max_heap) == 1:
			running_medians.append(min_heap[0])
		else:
			running_medians.append(float(-max_heap[0] + min_heap[0])/2)
	
	#running_medians = [median(uniq_wc_list[:i]) for i in range(1, len(uniq_wc_list)+1)]

	# Write out the running medians to OUTPUT_PATH
	with open (OUTPUT_PATH, 'w') as output:
		for median in running_medians[:-1]:
			output.write("{}\n".format(float(median)))
		output.write("{}\n".format(float(running_medians[-1])))

def main():
	INPUT_PATH = sys.argv[1]
	OUTPUT_PATH = sys.argv[2]
	uniq_wc_list = map_tweet_to_unique_wc(INPUT_PATH)
	calculate_running_median(uniq_wc_list, OUTPUT_PATH)

if __name__ == '__main__':
	main()