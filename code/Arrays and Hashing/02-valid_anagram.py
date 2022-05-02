# EASY
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# a = "anagram", t = "nagaram" a is an anagram of t

str1 = "anagram"
str2 = "angAraM"

def isAnagram(input1,input2):
    hashset = set()
    count = 0
    if len(input1) != len(input2):
        return False
    for i1 in input1.lower():
        hashset.add(i1)
    for i2 in input2.lower():
        if i2 in hashset:
            count = count+1
    if count == len(input1):
        return True
    return False

print(isAnagram(str1, str2))