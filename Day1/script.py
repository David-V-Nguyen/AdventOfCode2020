# Read the text file and store in variable f
f = open('Day1/input.txt')

# reads and stores all integers in an array, stored in num variable
num = f.readlines()

print(num)

# map is a function applies functions to a given list
# Loops by itself
# strip removes spaces and new line characters
lines = list(map(str.strip, num))

#print(list(lines))

# store the input of values within its list inside lines 
lines = list(lines)

# Loop through collection 'lines' and cast each item string => integer
values = []
for x in lines: # x is every single item
    values.append(int(x)) # 'collection'.append(), adds to the collection
    
print(values)

# Add 2 values if they equal 2020, multiply them together
'''
def calculateTwoValues():
    i = 0
    while i < len(values):
        if 2020 - values[i] in values:     # i = item in values
            print(values[i] * (2020 - values[i]))
        i+=1
'''
def calculateTwoValues():
    for i in values:
        if 2020 - i in values:  # 2020 - i = ???
            print(i * (2020 - i))

calculateTwoValues()

# Add 3 values if the equal 2020, multiply them together
def calculateThreeValues():
    for i in values:
        for p in values:
            if 2020 - i - p in values:
                print(i * (2020 - i - p) * (p)) # 3rd value = (2020 - i - p)

calculateThreeValues()
