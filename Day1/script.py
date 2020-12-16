# Read the text file and store in variable f
f = open('Day1/input.txt')

# reads and stores all integers in an array, stored in num variable
num = f.readlines()

print(num)

# map is a function applies functions to a given list
# Loops by itself
# strip removes spaces and new line characters
lines = list(map(str.strip, num))

print(list(lines))

# store the input of values within its list inside cleanLines 
cleanLines = list(lines)

int(cleanLines)

# 
x = 0
for x in int(cleanLines): 
    print("hello world")