"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s
"""
s = 'azcbobobegghakl'
lengthofs = len(s)
stringToFind = 'bob'
count = 0
for i in range(lengthofs):
    if s[i:i+3] == stringToFind:
        count += 1
print("Number of times bob occurs is: " + str(count))