### insight-data-eng-coding-challenge

This challenge is to implement two features:

* Calculate the total number of times each word has been tweeted.
* Calculate the median number of unique words per tweet, and update this median as tweets come in.

To execute the programs, please execute run.sh as an executable. The output of the programs can be found under tweet_output

### Organization:

* The first program leverage a defaultdict data structure to keep track of word frequency, and it assumes that the dictionary fits into memory
* The second program calculates the running median. It assumes that the unique word counts of all tweets fit into memory. The running median calculation can be done in 1 pass of the data since we leverage/maintain a min-heap and a max-heap to keep track of the median at any given point. 
