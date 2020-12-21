import re as re

# store the data in variable f
f = open('Day2/input.txt')

# read the data in f and assign it to variable passwords
words = f.readlines()

#print(words)

# remove the spaces and '\n' from the data
#passwords = list(map(str.strip, words))

passwords = list(map(str.strip, words))

#print(passwords)

# Sort the rules and passwords for each item in collection using dictionary??

# Separate rules from passwords

correct_passwords = []
for i in passwords: # i = single password
    #rules.append(re.split('[1-9][0-9]?', i))
    match = re.match(r"([1-9][0-9]?)\-([1-9][0-9]?) ([a-z]): ([a-z]+)", i) 
    min_, max_, character, password = match.groups() # tuple above is unpacked
    min_ = int(min_)
    max_ = int(max_)
    c = password.count(character)
    if min_ <= c <= max_: # '=>' this is an operator, some weird shit
        correct_passwords.append(password)
    print(c)

print(len(correct_passwords))

# 1 - 3 = either position 1 and 2 must have the character to be correct
# 
# Find the number of correct passwords 
valid_count = 0
for i in passwords: # i = single password
    #rules.append(re.split('[1-9][0-9]?', i))
    match = re.match(r"([1-9][0-9]?)\-([1-9][0-9]?) ([a-z]): ([a-z]+)", i) 
    pos_a, pos_b, character, password = match.groups() # tuple above is unpacked
    print(match.groups())
    pos_a = int(pos_a)
    pos_b = int(pos_b)
    occurrences = 0
    #index_a = pos_a - 1 
    if password[pos_a-1] == character:
        occurrences +=1

    if password[pos_b-1] == character:
        occurrences +=1  

    if occurrences == 1:
        valid_count +=1

print(valid_count)

