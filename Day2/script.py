import re as re

# store the data in variable f
f = open('Day2/input.txt')

# read the data in f and assign it to variable passwords
words = f.readlines()

# remove the spaces and '\n' from the data
passwords = list(map(str.strip, words))

print(passwords)

# Sort the rules and passwords for each item in collection using dictionary??

# Separate rules from passwords
rules = []
for i in passwords: # i = password
    rules.append(re.split('r[1-20]\s\w:', i))

print(rules)

# Convert rules from string => integer
numRules = []
for x in rules:
    numRules.append(int(x))

print(numRules)

# Separate password phrase from rules
'''
passPhrase = []
for p in passwords:
    passPhrase.append(re.split('r[a-z]', p))

print(passPhrase)
'''

# Create a dictionary for the rules and passwords



# Check if the passwords match the rules stated

# If password is true to rules then store entry in variable 'correctPasswords'
correctPasswords = []


# Find and Display number of total correct passwords 

