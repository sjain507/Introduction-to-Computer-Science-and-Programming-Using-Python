"""
Problem Statement: Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
"""
#s= 'azcbobobegghakl'
vowels = 'aeiou'
count = 0
for letters in s:
    if letters in vowels:
        count += 1
print ("Number of vowels: ",  str(count))