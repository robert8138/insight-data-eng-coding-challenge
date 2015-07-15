#!/usr/bin/env bash

# The two external python library I used are heapq & collections
# If these packages are missing, please install them using pip
# pip install heapq
# pip install collections

# Make sure the python files are executable
chmod a+x ./src/words_tweeted.py
chmod a+x ./src/median_unique.py

# Execute the following command from the root directory
python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt



