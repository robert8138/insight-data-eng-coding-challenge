from numpy import median
from collections import defaultdict
import sys

def map_tweet_to_unique_wc(INPUT_PATH):
	'''(string) -> defaultdict(set)

	For each tweet in INPUT_PATH, tokenize the tweet and count the 
	number of unique token using Functional programming style 
	specifically, Map operation 
	'''
	with open(INPUT_PATH, 'r') as tweets:
		return map(lambda tweet: len(set(tweet.split())), tweets)

def calculate_running_median(uniq_wc_list, OUTPUT_PATH):
	'''(list, string) -> None
	
	Take one pass of the uniq_wc_list and compute running median
	using a min-heap and a max-heap
	'''
	#pdb.set_trace()
	running_median = []
	first_count = uniq_wc_list.pop(0)
	if uniq_wc_list:
		second_count = uniq_wc_list.pop(0)
		if first_count >= second_count:
			min_heap = [first_count] # smaller than everything in this heap
			max_heap = [-second_count] # larger than everything in this heap
		else:
			min_heap = [second_count]
			max_heap = [-first_count]
		running_median.append(first_count)
		running_median.append(float(min_heap[0] - max_heap[0])/2)
	else:
		min_heap = [first_count]
		running_median.append(first_count)

	while uniq_wc_list:
		# Process a new record
		count = uniq_wc_list.pop(0)
		if count >= min_heap[0]:
			heapq.heappush(min_heap, count)
		elif count < -max_heap[0]: 	
			heapq.heappush(max_heap, -count)
		else:
			heapq.heappush(max_heap, -count)
		# Rebalance the heap structures to be off by 1 element
		if len(max_heap) - len(min_heap) > 1:
			heapq.heappush(min_heap, -heapq.heappop(max_heap))
		elif len(min_heap) - len(max_heap) > 1:
			heapq.heappush(max_heap, -heapq.heappop(min_heap))

		# Calculate Median
		if len(max_heap) - len(min_heap) == 1:
			running_median.append(-max_heap[0])
		elif len(min_heap) - len(max_heap) == 1:
			running_median.append(min_heap[0])
		else:
			running_median.append(float(-max_heap[0] + min_heap[0])/2)
	#return running_median
	
	# Use list comprehension to calculate median 
	# This is not efficient, we can do this in one pass
	# Using one min heap and one max heap
	#running_medians = [median(uniq_wc_list[:i]) for i in range(1, len(uniq_wc_list)+1)]
	# [1.0, 2.0, 3.0, 17.5, 8.0, 19.5, 8.0, 19.5]

	# Write out the running medians to OUTPUT_PATH
	with open (OUTPUT_PATH, 'w') as output:
		for med in running_medians[:-1]:
			output.write("{}\n".format(med))
		output.write("{}\n".format(running_medians[-1]))

def main():
	INPUT_PATH = sys.argv[1]
	OUTPUT_PATH = sys.argv[2]
	uniq_wc_list = map_tweet_to_unique_wc(INPUT_PATH)
	calculate_running_median(uniq_wc_list, OUTPUT_PATH)

if __name__ == '__main__':
	main()