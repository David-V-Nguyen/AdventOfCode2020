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

# store the input of values within its list inside lines 
lines = list(lines)

# Loop through collection 'lines' and cast each item string => integer
values = []
for x in lines: # x is every single item
    values.append(int(x)) # 'collection'.append(), adds to the collection
    
print(values)

# Add 2 values if they equal 2020, multiply them together
def calculateTwoValues(a, b):
    while i <= len(values):
        while m <= len(values):
            values.range([2])
            if a + b == 2020:
            