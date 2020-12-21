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
    match = re.match(r"([1-9][0-9]?)\-([1-9][0-9]?) ([a-z]): ([a-z]+)", i) # raw string, finds min num, space, finds max num, space, finds char,:, finds password with/without multi chars
    min_, max_, character, password = match.groups() # tuple above is unpacked
    min_ = int(min_) # min number of appearances
    max_ = int(max_) # max number of appearances
    c = password.count(character) # finds the number of certain character in a password
    if min_ <= c <= max_: # '=>' this is an operator, some weird shit
        correct_passwords.append(password) # store the correct passwords
    print(c)

print(len(correct_passwords)) # print the length property of the correct_passwords

# 1 - 3 = either position 1 and 2 must have the character to be correct
# 
# Find the number of correct passwords 
valid_count = 0
for i in passwords: # i = single password
    match = re.match(r"([1-9][0-9]?)\-([1-9][0-9]?) ([a-z]): ([a-z]+)", i) # re.match() allows 
    pos_a, pos_b, character, password = match.groups() # tuple above is unpacked, '___.groups() allows entire regex variables to be displayed  
    print(match.groups())
    pos_a = int(pos_a) # change pos_a into integer
    pos_b = int(pos_b) # change pos_b into integer
    occurrences = 0
    #index_a = pos_a - 1 
    if password[pos_a-1] == character: # finds if the password has similar characters defined in 1st position
        occurrences +=1

    if password[pos_b-1] == character: # finds if the password has similar characters defined in 2nd position
        occurrences +=1  # increment occurrences found

    if occurrences == 1: # finds if there are occurrences, then add to valid counter
        valid_count +=1

print(valid_count)

