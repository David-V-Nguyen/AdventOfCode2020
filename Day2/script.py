import re as re

# store the data in variable f
f = open('Day2/input.txt')

# read the data in f and assign it to variable passwords
words = f.readlines()

print(words)

# remove the spaces and '\n' from the data
passwords = list(map(str.strip, words))

print(passwords)

# 
rules = re.split('', passwords)